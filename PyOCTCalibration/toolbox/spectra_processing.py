
'''_____Standard imports_____'''
import numpy as np
import json
import scipy.fftpack as fp
import matplotlib.pyplot as plt
import sys

'''_____Project imports_____'''
from toolbox.filters import butter_highpass_filter
from toolbox.calibration_processing import linearize_spectra, compensate_dispersion
from toolbox.maths import spectra2aline


def process_Aline(spectra, calibration, arguments):

    spectra = np.array(spectra) + np.array(calibration['dark_not']) - np.array(calibration['dark_ref']) - np.array(calibration['dark_sample'])

    spectra = butter_highpass_filter(spectra, cutoff=180, fs=30000, order=5)

    spectra = linearize_spectra(spectra, calibration['klinear'])

    spectra = compensate_dispersion( np.array(spectra), arguments.dispersion * np.array( calibration['dispersion'] ) )

    Aline = spectra2aline(spectra)

    Aline = Aline[0:len(Aline)//2]

    return Aline


def process_Bscan(Spectra, calibration, arguments):

    Bscan = []

    for i, spectra in enumerate(Spectra):

        spectra = Spectra[i]

        Aline = process_Aline(spectra, calibration, arguments)

        Bscan.append(Aline)

    Bscan = np.array(Bscan)

    return Bscan


def denoise_Bscan(Bscan):

    F1 = fp.fft2((Bscan).astype(float))

    F2 = fp.fftshift(F1)

    F2[500:530,:] = 0

    (w, h) = Bscan.shape

    half_w, half_h = int(w/2), int(h/2)

    F2[0 :1024, half_h -1 : half_h + 1] = 0

    Bscan = np.abs(fp.ifft2(fp.ifftshift(F2)).real)

    return Bscan


def process_Cscan(Cscan_spectra):

    output_Cscan []

    for iteration, Bscan_spectra in enumerate(Cscan_spectra):

        print( '################## [{0}/{1}]'.format( iteration, length ) )

        Bscan = process_Bscan(Bscan_spectra, calibration, arguments)

        Bscan = denoise_Bscan(Bscan)

        output_Cscan.append(Bscan)

    return output_Cscan

# ---
