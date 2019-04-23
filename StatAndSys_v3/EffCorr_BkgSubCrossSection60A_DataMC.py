from ROOT import *
import ROOT as root
import numpy as np
from array import array

gStyle.SetOptStat(0)

#############################################################
## I use this new propagation method for the combined sample
## The only error propagated are the one associated with the 
## corrections
## the errors associated with the energy migration are 
## calculated separately

'''
MCName = "/Users/elenag/Desktop/BeamLineCompoForPion/MCCorrection/ErrorPropagationInXS/MC/MC_Staggered_Data60A.root"
MCFile = root.TFile(MCName)
XS_60APiOnly  = MCFile.Get("XS_60APiOnly")
XS_60APiOnly.SetFillColor(kWhite)
XS_60APiOnly.SetLineColor(kAzure)

XS_60APiOnly.SetBinContent(1,0)
XS_60APiOnly.SetBinContent(2,0)
XS_60APiOnly.SetBinContent(3,0)
#XS_60APiOnly.SetBinContent(4,0)
XS_60APiOnly.SetBinContent(15,0)
XS_60APiOnly.SetBinContent(16,0)
XS_60APiOnly.SetBinError(1,0)
XS_60APiOnly.SetBinError(2,0)
XS_60APiOnly.SetBinError(3,0)
#XS_60APiOnly.SetBinError(4,0)
XS_60APiOnly.SetBinError(15,0)
XS_60APiOnly.SetBinError(16,0)
'''


inFileName          = "../StatOnly/XSRaw_StatOnlyUnc_Data60A.root"
f                   = root.TFile(inFileName)
XS_Stat             = f.Get("XS_Out")
XS_Stat.SetBinContent(3,-100)
XS_Stat.SetBinError(3,0)



inFileNameSys          = "../Systematics/XSRaw_SysOnlyUnc_SystematicsEnergy60A.root"
fSys                  = root.TFile(inFileNameSys)
XS_SysMax             = fSys.Get("XS_ErrMax")
XS_SysMin             = fSys.Get("XS_ErrMin")


inFileNameBkg          = "../BkgSub_v3/BkgSubWithBuoundaries_60A.root"
fBkg                  = root.TFile(inFileNameBkg)
XS_BkgSub             = fBkg.Get("XS_BkgSub60A")
XS_BkgMax             = fBkg.Get("XS_BkgSub_Max60A")
XS_BkgMin             = fBkg.Get("XS_BkgSub_Min60A")


inFileNameEff          = "../EffCorrection_v3/Eff_Correction_60A_WithBoundaries.root"
fEff                  = root.TFile(inFileNameEff)
XS_Eff                = fEff.Get("XS_Eff")
XS_EffMax             = fEff.Get("XS_Eff_Max")
XS_EffMin             = fEff.Get("XS_Eff_Min")

cXSD = TCanvas("cXSD","cXSD",600,600)
cXSD.SetGrid()
XS_Eff.Draw("pe")
XS_EffMax.Draw("pesame")
XS_EffMin.Draw("pesame")


for i in xrange(16,30):
    XS_Eff.SetBinContent(i,-100)
    XS_Eff.SetBinError(i,0)

for i in xrange(5):
    XS_Eff.SetBinContent(i,-100)
    XS_Eff.SetBinError(i,0)

noRootFileName = "Plots60A_BkgSub_EffCorr"
#####################################################################
###################    Error Propagation   ##########################
#####################################################################

intMaxErr_CorrOnly, incMaxErr_CorrOnly, XSMaxErr_CorrOnly = array( 'd' ), array( 'd' ), array( 'd' )
intMinErr_CorrOnly, incMinErr_CorrOnly, XSMinErr_CorrOnly = array( 'd' ), array( 'd' ), array( 'd' )
intMaxErr_StaSys  , incMaxErr_StaSys  , XSMaxErr_StaSys   = array( 'd' ), array( 'd' ), array( 'd' )
intMinErr_StaSys  , incMinErr_StaSys  , XSMinErr_StaSys   = array( 'd' ), array( 'd' ), array( 'd' )
intErr_Central    , incErr_Central    , XSErr_Central     = array( 'd' ), array( 'd' ), array( 'd' )
x                 , exl               , exh               = array( 'd' ), array( 'd' ), array( 'd' )

for i in xrange(XS_Stat.GetSize()):

    bin_XS_Eff    = XS_Eff   .GetBinContent(i)   
    bin_XS_EffMax = XS_EffMax.GetBinContent(i)  
    bin_XS_EffMin = XS_EffMin.GetBinContent(i)  
    err_XS_EffMax = bin_XS_EffMax - bin_XS_Eff  
    err_XS_EffMin = bin_XS_Eff    - bin_XS_EffMin

    
    bin_XS_BkgSub = XS_BkgSub.GetBinContent(i)   
    bin_XS_BkgMax = XS_BkgMax.GetBinContent(i)  
    bin_XS_BkgMin = XS_BkgMin.GetBinContent(i)  

    err_XS_BkgMax = bin_XS_BkgMax - bin_XS_BkgSub  
    err_XS_BkgMin = bin_XS_BkgSub - bin_XS_BkgMin

    statErrXS         = XS_Stat  .GetBinError(i)
    sysMaxXS          = XS_SysMax.GetBinError(i)
    sysMinXS          = XS_SysMin.GetBinError(i)


    XSMaxErr_CorrOnly  .append(TMath.Sqrt( err_XS_BkgMax*err_XS_BkgMax + err_XS_EffMax*err_XS_EffMax))
    XSMinErr_CorrOnly  .append(TMath.Sqrt( err_XS_BkgMin*err_XS_BkgMin + err_XS_EffMin*err_XS_EffMin))

    XSMaxErr_StaSys  .append(TMath.Sqrt(statErrXS*statErrXS + sysMaxXS*sysMaxXS + err_XS_BkgMax*err_XS_BkgMax + err_XS_EffMax*err_XS_EffMax))
    XSMinErr_StaSys  .append(TMath.Sqrt(statErrXS*statErrXS + sysMinXS*sysMinXS + err_XS_BkgMin*err_XS_BkgMin + err_XS_EffMin*err_XS_EffMin))
    XSErr_Central    .append(XS_Eff            .GetBinContent(i))
    XS_Stat.SetBinContent(i, XS_Eff            .GetBinContent(i))

    x   .append(-125+50*i)
    exl .append(25.)
    exh .append(25.)

grXS          = TGraphAsymmErrors(XS_Stat.GetSize(),x,XSErr_Central ,exl,exh,XSMinErr_StaSys ,XSMaxErr_StaSys);
grXSCorrOnly  = TGraphAsymmErrors(XS_Stat.GetSize(),x,XSErr_Central ,exl,exh,XSMinErr_CorrOnly , XSMaxErr_CorrOnly);

grXS.SetLineColor(kRed)
grXS.SetFillColor(kWhite)


#####################################################################
#######################    Aestetics   ##############################
#####################################################################

lariatHead = TLatex();
lariatHead.SetNDC();
lariatHead.SetTextFont(62);
lariatHead.SetTextSize(0.04);
lariatHead.SetTextAlign(40);


XS_Stat            .SetFillColor(kWhite)
XS_Stat            .SetLineColor(kBlack)
XS_Stat            .SetMarkerStyle(8)
XS_Stat            .SetMarkerSize(0.5)

grXS.SetTitle("; Kinetic Energy [MeV]; #sigma_{#pi} per 50 MeV [barn]")
XS_Stat            .GetYaxis().SetTitleOffset(1.2)


cXS = TCanvas("cXS","cXS",600,600)
cXS.SetGrid()
grXS.GetXaxis().SetRangeUser(0,1200.)
grXS.GetYaxis().SetRangeUser(0,4.)
grXS.Draw("AP")
#MC_XS.Draw("histosame][")
#XS_60APiOnly.Draw("histosame][")
grXS.Draw("P")
XS_Stat.Draw("e0same")

lariatHead.DrawLatex(0.6,0.90,"LArIAT Preliminary");
#lariatHead.DrawLatex(0.13,0.84,"same"); 
legendXS = TLegend(.44,.65,.90,.90)
legendXS.AddEntry(XS_Stat," -60A Data Stat Only");
legendXS.AddEntry(grXS,   " -60A Data Stat and Sys");
#legendXS.AddEntry(XS_60APiOnly,  "MC Reco -60A #pi Only");

legendXS.Draw("same")
cXS.Update()
cXS.SaveAs(noRootFileName+"_MCData_XS_StatSyst_BkgSub_EffCorr.pdf")

#####################################################################
#######################    Save to File   ###########################
#####################################################################
outFile = TFile("Final60A.root","recreate")
outFile.cd()
grXS.Write("grXS60A")
grXSCorrOnly.Write("grXS60A_CorrOnly")
XS_Stat.Write("XS60A_StatOnly")


outFile.Write()
outFile.Close()
raw_input()

