import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import common_tools as ct
import mplhep as hep
import os

plt.style.use([hep.style.ROOT])
plt.rc('text', usetex=True)
mpl.use('Agg')

cms_4l = ct.plotData(*ct.plotDataFromFile("data/ZZ_CMS_measurements.txt"), label=r"CMS $2\ell2\ell\prime$")
cms_2l2v = ct.plotData(*ct.plotDataFromFile("data/ZZ_2l2v_CMS_measurements.txt"), label=r"CMS $2\ell2\nu$")
atlas_4l = ct.plotData(*ct.plotDataFromFile("data/ZZ_ATLAS_measurements.txt"), label=r"ATLAS $2\ell2\ell\prime$ (x1.016)")
atlas_2l2v = ct.plotData(*ct.plotDataFromFile("data/ZZ_2l2v_ATLAS_measurements.txt"), label=r"ATLAS $2\ell2\ell\prime+2\ell2\nu$ (x1.016)")

(x,y,systup, systdown, statup, statdown) = ct.plotDataFromFile("data/ZZ_nnlo_nloew_values.txt")
nnlo = plt.plot(x,y,'#002D80', zorder=1)
nnlo_fill = plt.fill_between(x, [i+e for i,e in zip(y, systup)], [i-e for i,e in zip(y, systdown)], color='#A3DFFF',alpha=.8, zorder=1)

(x,y,systup, systdown, statup, statdown) = ct.plotDataFromFile("data/ZZ_scan_values_removebr_fixedscale.txt")
nlo = plt.plot(x,y, '#ca0020', dashes=[10, 5,], label="", zorder=1)
nlo_fill = plt.fill_between(x, [i+e for i,e in zip(y, systup)], [i-e for i,e in zip(y, systdown)], color='#FFE6EC',alpha=.4, zorder=1)


plt.xlim(6.5,14.1)
plt.ylim(2,20)
plt.locator_params(axis='y', nbins=6)
plt.locator_params(axis='x', nbins=6)
plt.xticks(fontsize=26)
plt.yticks(fontsize=26)
plt.ylabel(r"$\sigma_{\mathrm{pp}\to\mathrm{ZZ}}$  [pb]", fontsize=30, horizontalalignment='right', y=1.0)
plt.xlabel("$\sqrt{s}$  [TeV]", fontsize=30, horizontalalignment='right', x=1.0)

leg = plt.legend([cms_4l[0], cms_2l2v[0], atlas_4l[0], atlas_2l2v[0], (nnlo[0], nnlo_fill), (nlo[0], nlo_fill)], 
        [
            r"CMS $2\ell2\ell^{\prime}$",
            r"CMS $2\ell2\nu$",
            r"ATLAS $2\ell2\ell^{\prime}$ \Large{(x1.016)}",
            r"ATLAS $2\ell2\ell^{\prime}+2\ell2\nu$ \Large{(x1.016)}",
            "MATRIX \LARGE{qq[NNLOxNLO EW]+ggNLO}\n"+ \
               r"\Large{NNPDF3.1luxQED}, $\mu_{\mathrm{R}} = \mu_{\mathrm{F}} = m_{\mathrm{Z}}$", 
            "MCFM qqNLO+ggLO\n" + \
               r"\Large{NNPDF3.0}, $\mu_{\mathrm{R}} = \mu_{\mathrm{F}} = m_{\mathrm{Z}}$", 
    ], loc='upper left', fontsize=20
)
#leg.legendHandles[0]._sizes = [100]
#leg.legendHandles[1]._sizes = [100]

fig = plt.gcf()
fig.savefig(os.path.expanduser("~/www/DibosonPlots/ZZCrossSection_{:%Y-%m-%d}.pdf".format(datetime.datetime.today())))


