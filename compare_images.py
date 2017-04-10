import math
from PIL import Image
import Levenshtein
import os,re,sys

class BWImageCompare(object):
    """Compares two images (b/w)."""

    _pixel = 255
    _colour = False

    def __init__(self, imga, imgb, maxsize=64):
        """Save a copy of the image objects."""

        sizea, sizeb = imga.size, imgb.size

        newx = min(sizea[0], sizeb[0], maxsize)
        newy = min(sizea[1], sizeb[1], maxsize)

        # Rescale to a common size:
        imga = imga.resize((newx, newy), Image.BICUBIC)
        imgb = imgb.resize((newx, newy), Image.BICUBIC)

        if not self._colour:
            # Store the images in B/W Int format
            imga = imga.convert('I')
            imgb = imgb.convert('I')

        self._imga = imga
        self._imgb = imgb

        # Store the common image size
        self.x, self.y = newx, newy

    def _img_int(self, img):
        """Convert an image to a list of pixels."""

        x, y = img.size

        for i in xrange(x):
            for j in xrange(y):
                yield img.getpixel((i, j))

    @property
    def imga_int(self):
        """Return a tuple representing the first image."""

        if not hasattr(self, '_imga_int'):
            self._imga_int = tuple(self._img_int(self._imga))

        return self._imga_int

    @property
    def imgb_int(self):
        """Return a tuple representing the second image."""

        if not hasattr(self, '_imgb_int'):
            self._imgb_int = tuple(self._img_int(self._imgb))

        return self._imgb_int

    @property
    def mse(self):
        """Return the mean square error between the two images."""

        if not hasattr(self, '_mse'):
            tmp = sum((a-b)**2 for a, b in zip(self.imga_int, self.imgb_int))
            self._mse = float(tmp) / self.x / self.y

        return self._mse

    @property
    def psnr(self):
        """Calculate the peak signal-to-noise ratio."""

        if not hasattr(self, '_psnr'):
            self._psnr = 20 * math.log(self._pixel / math.sqrt(self.mse), 10)

        return self._psnr

    @property
    def nrmsd(self):
        """Calculate the normalized root mean square deviation."""

        if not hasattr(self, '_nrmsd'):
            self._nrmsd = math.sqrt(self.mse) / self._pixel

        return self._nrmsd

    @property
    def levenshtein(self):
        """Calculate the Levenshtein distance."""

        if not hasattr(self, '_lv'):
            stra = ''.join((chr(x) for x in self.imga_int))
            strb = ''.join((chr(x) for x in self.imgb_int))

            lv = Levenshtein.distance(stra, strb)

            self._lv = float(lv) / self.x / self.y

        return self._lv


class ImageCompare(BWImageCompare):
    """Compares two images (colour)."""

    _pixel = 255 ** 3
    _colour = True

    def _img_int(self, img):
        """Convert an image to a list of pixels."""

        x, y = img.size

        for i in xrange(x):
            for j in xrange(y):
                pixel = img.getpixel((i, j))
                yield pixel[0] | (pixel[1]<<8) | (pixel[2]<<16)

    @property
    def levenshtein(self):
        """Calculate the Levenshtein distance."""

        if not hasattr(self, '_lv'):
            stra_r = ''.join((chr(x>>16) for x in self.imga_int))
            strb_r = ''.join((chr(x>>16) for x in self.imgb_int))
            lv_r = Levenshtein.distance(stra_r, strb_r)

            stra_g = ''.join((chr((x>>8)&0xff) for x in self.imga_int))
            strb_g = ''.join((chr((x>>8)&0xff) for x in self.imgb_int))
            lv_g = Levenshtein.distance(stra_g, strb_g)

            stra_b = ''.join((chr(x&0xff) for x in self.imga_int))
            strb_b = ''.join((chr(x&0xff) for x in self.imgb_int))
            lv_b = Levenshtein.distance(stra_b, strb_b)

            self._lv = (lv_r + lv_g + lv_b) / 3. / self.x / self.y

        return self._lv


class FuzzyImageCompare(object):
    """Compares two images based on the previous comparison values."""

    def __init__(self, imga, imgb, lb=1, tol=15):
        """Store the images in the instance."""

        self._imga, self._imgb, self._lb, self._tol = imga, imgb, lb, tol

    def compare(self):
        """Run all the comparisons."""

        if hasattr(self, '_compare'):
            return self._compare

        lb, i = self._lb, 2

        diffs = {
            'levenshtein': [],
            'nrmsd': [],
            'psnr': [],
        }

        stop = {
            'levenshtein': False,
            'nrmsd': False,
            'psnr': False,
        }

        while not all(stop.values()):
            cmp = ImageCompare(self._imga, self._imgb, i)

            diff = diffs['levenshtein']
            if len(diff) >= lb+2 and \
                abs(diff[-1] - diff[-lb-1]) <= abs(diff[-lb-1] - diff[-lb-2]):
                stop['levenshtein'] = True
            else:
                diff.append(cmp.levenshtein)

            diff = diffs['nrmsd']
            if len(diff) >= lb+2 and \
                abs(diff[-1] - diff[-lb-1]) <= abs(diff[-lb-1] - diff[-lb-2]):
                stop['nrmsd'] = True
            else:
                diff.append(cmp.nrmsd)

            diff = diffs['psnr']
            if len(diff) >= lb+2 and \
                abs(diff[-1] - diff[-lb-1]) <= abs(diff[-lb-1] - diff[-lb-2]):
                stop['psnr'] = True
            else:
                try:
                    diff.append(cmp.psnr)
                except ZeroDivisionError:
                    diff.append(-1)  # to indicate that the images are identical

            i *= 2

        self._compare = {
            'levenshtein': 100 - diffs['levenshtein'][-1] * 100,
            'nrmsd': 100 - diffs['nrmsd'][-1] * 100,
            'psnr': diffs['psnr'][-1] == -1 and 100.0 or diffs['psnr'][-1],
        }

        return self._compare

    def similarity(self):
        """Try to calculate the image similarity."""

        cmp = self.compare()

        lnrmsd = (cmp['levenshtein'] + cmp['nrmsd']) / 2
        return lnrmsd
        return min(lnrmsd * cmp['psnr'] / self._tol, 100.0)  # TODO: fix psnr!


def extract_key_frame(dir):
    #dir = sys.argv[1]
    file = os.listdir(dir)

    tot = len(file)
    print 'Comparing %d images:' % tot

    curDir = os.getcwd()
    os.chdir(dir)

    images = {}
    for img in file:

        if img.endswith("jpg"):
            images[img] = Image.open(img)
    os.chdir(curDir)

    results, i = {}, 1

    keys = images.keys()
    dif = []
    keys.sort()
    for index,img in enumerate(keys):
        if index < len(keys)-2:
            namea = img
            nameb = keys[index+1]
            imga = images[namea]
            imgb = images[nameb]
            cmp = FuzzyImageCompare(imga, imgb)
            sim = cmp.similarity()
            results[(namea, nameb)] = sim
            if sim < 45.0:
                dif.append(nameb)
                print ' * %2d / %2d:' % (i, tot),
                print namea, nameb, '...',
                print '%.2f %%' % sim
            i += 1

    dif.sort()
    print "********************"
    result = [keys[0]]
    dif.reverse()
    for index,img in enumerate(dif) :
        if index < len(dif)-2:
            if abs(int(re.findall(r'(\w*[0-9]+)\w*',dif[index])[0]) - int(re.findall(r'(\w*[0-9]+)\w*',dif[index+1])[0])) != 1:
                result.append(img)
    result.sort()
    print result
    return result

def extract_key_frame_time(dir):
    key_frame = extract_key_frame(dir)
    time = []
    for img in key_frame:
        time.append(int(re.findall(r'(\w*[0-9]+)\w*',img)[0]))

    seg = 0
    needed_key_frame_time = [0]#save the time of every needed key frame
    needed_key_frame = [key_frame[0]]
    for i in time:
        if i > seg + 6:
            needed_key_frame_time.append(i-1)
            for frame in key_frame:
                if int(re.findall(r'(\w*[0-9]+)\w*',frame)[0])== i:
                    needed_key_frame.append(frame)
            seg = i

    needed_key_frame_length = []#save the length of every music episode
    for index,i in enumerate(needed_key_frame_time):
        if index < len(needed_key_frame_time)-1:
            leng = needed_key_frame_time[index+1] - needed_key_frame_time[index]
            needed_key_frame_length.append(leng)
    curDir = os.getcwd()
    os.chdir(dir)
    for image in os.listdir(dir):
        if image not in needed_key_frame:
            os.remove(image)
    os.chdir(curDir)       
    
    return needed_key_frame_length,needed_key_frame

if __name__ == '__main__':

    length,frame = extract_key_frame_time("/home/xiat/music_generation/test_image")
    for i in length:
        print i
    for i in frame:
        print i


