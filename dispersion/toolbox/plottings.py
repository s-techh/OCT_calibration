
'''_____Standard imports_____'''
import numpy as np
import matplotlib.pyplot as plt


'''_____Project imports_____'''
from toolbox.fits import gauss


def dB_plot(data1, data2=None):

    fig = plt.figure(figsize=(15, 6))

    if data2 is None:
        ax = fig.add_subplot(111)
        ref1 = np.min(data1)
        dB1 = 10 * np.log(data1/ref1)
        ax.plot(dB1)
        ax.grid()
        ax.set_ylabel('Magnitude [dB]')
        ax.set_xlabel('Wavenumber k [U.A]')

    else:
        ax0 = fig.add_subplot(121)
        ax1 = fig.add_subplot(122)

        ref1 = np.max(data1)
        ref2 = np.max(data2)

        dB1 = 10 * np.log(data1/ref1)
        dB2 = 10 * np.log(data2/ref2)

        ax0.plot(dB1)
        ax0.set_title('Processed Aline')
        ax0.grid()
        ax0.set_ylabel('Magnitude [dB]')
        ax0.set_xlabel('Wavenumber k [U.A]')

        ax1.plot(dB2)
        ax1.set_title('Raw Aline')
        ax1.grid()
        ax1.set_ylabel('Magnitude [dB]')
        ax1.set_xlabel('Wavenumber k [U.A]')
        ax1.set_ylim(ax0.get_ylim())

    plt.waitforbuttonpress()
    plt.close()


def interactive_shift(spectra1, param1, spectra2, param2):


    shift1_condition = False
    shift2_condition = False

    while shift1_condition is False:

        shifted_spectra_plots( spectra1,
                               param1,
                               spectra2,
                               param2 )

        shift1 = input("Shift mirror1? [>0:Left, 0:None, <0:Right]")
        shift1 = eval(shift1)

        if shift1 == 0:
            shift1_condition = True
        else:
            print(param1[2])
            param1[2] += shift1
        plt.close()


    while shift2_condition is False:

        shifted_spectra_plots( spectra1,
                               param1,
                               spectra2,
                               param2 )

        shift2 = input("Shift mirror1? [>0:Left, 0:None, <0:Right]")
        shift2 = eval(shift2)

        if shift2 == 0:
            shift2_condition = True
        else:
            param2[2] += shift2
        plt.close()


def shifted_spectra_plots(spectra1, param1, spectra2, param2):

    plt.ion()
    fig = plt.figure(figsize=(15, 6))
    ax0 = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)


    ax0.plot( spectra1, label='Shifted raw' )
    ax0.grid()
    ax0.set_title('Shifted raw spectra mirror 1')

    ax0.plot( gauss(*param1),'r-', label='gaussian fit' )
    ax0.grid()
    ax0.set_title('Fitted gaussian curve mirror 1')

    ax1.plot( spectra2, label='Shifted raw' )
    ax1.grid()
    ax1.set_title('Shifted raw spectra mirror 2')

    ax1.plot( gauss(*param2), 'r-', label='gaussian fit' )
    ax1.grid()
    ax1.set_title('Fitted gaussian curve mirror 2')

    print("click the image to exit")
    ax0.legend()
    ax0.grid()

    ax1.legend()
    ax1.grid()
    fig.canvas.draw()


def phase_dispersion_plot(exp_dispersion, fit_dispersion):

    fig = plt.figure(figsize=(15, 6))
    ax0 = fig.add_subplot(111)

    ax0.plot(fit_dispersion, label = 'fitted ')
    ax0.plot(exp_dispersion,'*',label = 'experimental')

    ax0.set_ylabel('Unwrapped phase [U.A]')
    ax0.set_title('System phase dispersion')
    plt.grid()
    plt.legend()

    print("click the image to exit")
    plt.waitforbuttonpress()
    plt.close()







# -
