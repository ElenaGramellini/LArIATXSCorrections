from ROOT import *
import ROOT as root
import numpy as np
from array import array

gStyle.SetOptStat(0)


inFileName      = "../StatAndSys_v2/Final60A.root"
fCompare60A     = root.TFile(inFileName)
XS60A_Comp      = fCompare60A.Get("XS60A_StatOnly")
gr60A_Comp      = fCompare60A.Get("grXS60A_CorrOnly")

inFileNameStat = "../StatOnly/XSRaw_StatOnlyUnc_Data60A.root"
fStat60A          = root.TFile(inFileNameStat)
int60A_Stat       = fStat60A.Get("hInteractingKE_Out")
inc60A_Stat       = fStat60A.Get("hIncidentKE_Out")

inFileNameEff_60A     = "../EffCorrection_v3/Eff_Correction_60A.root"
fEff_60A              = root.TFile(inFileNameEff_60A)
eff_Corr_45_Int_60A   = fEff_60A.Get("eff_Corr_45_Int_60A")
eff_Corr_45_Inc_60A   = fEff_60A.Get("eff_Corr_45_Inc_60A")

inFileNameBkg_60A     = "../BkgSub_v3/bkgFiles/BkgSub_1.0muons_1.0electrons_60A.root"
fBkg_60A              = root.TFile(inFileNameBkg_60A)
pion_Content_Int_60A  = fBkg_60A.Get("pion_Content_Int_60A")
pion_Content_Inc_60A  = fBkg_60A.Get("pion_Content_Inc_60A")

## Get the shifted distributions for the 60A
inFileSysName_60A       = "../Systematics/SystematicsEnergy60A.root"
fSys_60A                = root.TFile(inFileSysName_60A)
hInteractingKEMax_60A   = fSys_60A.Get("hInteractingKEMax")
hIncidentKEMax_60A      = fSys_60A.Get("hIncidentKEMax")
hInteractingKEMin_60A   = fSys_60A.Get("hInteractingKEMin")
hIncidentKEMin_60A      = fSys_60A.Get("hIncidentKEMin")



# This is the central point as calculated with the 60A for the interacting and incident
int60A_Stat.Multiply(pion_Content_Int_60A)
int60A_Stat.Divide(eff_Corr_45_Int_60A)
inc60A_Stat.Multiply(pion_Content_Inc_60A)
inc60A_Stat.Divide(eff_Corr_45_Inc_60A)


cXS_60 = TCanvas("cXS_60","cXS_60",600,600)
cXS_60.SetGrid()
inc60A_Stat.Draw("pe")
cXS_60.Update()

int60A_StatC = int60A_Stat.Clone("int60A_StatC")
inc60A_StatC = inc60A_Stat.Clone("inc60A_StatC")

int60A_StatC.Scale(101.)
int60A_StatC.Divide(inc60A_StatC)


####################################################################################
####################################################################################
####################################################################################

inFileName       = "../StatAndSys_v2/Final100A.root"
fCompare100A     = root.TFile(inFileName)
XS100A_Comp      = fCompare100A.Get("XS100A_StatOnly")
gr100A_Comp      = fCompare100A.Get("grXS100A_CorrOnly")



inFileNameStat = "../StatOnly/XSRaw_StatOnlyUnc_Data100A.root"
fStat100A          = root.TFile(inFileNameStat)
int100A_Stat       = fStat100A.Get("hInteractingKE_Out")
inc100A_Stat       = fStat100A.Get("hIncidentKE_Out")

inFileNameEff_100A     = "../EffCorrection/Eff_Correction_100A.root"
fEff_100A              = root.TFile(inFileNameEff_100A)
eff_Corr_45_Int_100A   = fEff_100A.Get("eff_Corr_45_Int_100A")
eff_Corr_45_Inc_100A   = fEff_100A.Get("eff_Corr_45_Inc_100A")

inFileNameBkg_100A     = "../BkgSub/bkgFiles/BkgSub_1.0muons_1.0electrons_100A.root"
fBkg_100A              = root.TFile(inFileNameBkg_100A)
pion_Content_Int_100A  = fBkg_100A.Get("pion_Content_Int_100A")
pion_Content_Inc_100A  = fBkg_100A.Get("pion_Content_Inc_100A")

## Get the shifted distributions for the 100A
inFileSysName_100A       = "../Systematics/SystematicsEnergy100A.root"
fSys_100A                = root.TFile(inFileSysName_100A)
hInteractingKEMax_100A   = fSys_100A.Get("hInteractingKEMax")
hIncidentKEMax_100A      = fSys_100A.Get("hIncidentKEMax")
hInteractingKEMin_100A   = fSys_100A.Get("hInteractingKEMin")
hIncidentKEMin_100A      = fSys_100A.Get("hIncidentKEMin")

# This is the central point as calculated with the 60A for the interacting and incident
int100A_Stat.Multiply(pion_Content_Int_100A)
int100A_Stat.Divide(eff_Corr_45_Int_100A)
inc100A_Stat.Multiply(pion_Content_Inc_100A)
inc100A_Stat.Divide(eff_Corr_45_Inc_100A)

int100A_StatC = int100A_Stat.Clone("int100A_StatC")
inc100A_StatC = inc100A_Stat.Clone("inc100A_StatC")

int100A_StatC.Scale(101.)
int100A_StatC.Divide(inc100A_StatC)


cXS100A = TCanvas("cXS100A","cXS100A",600,600)
cXS100A.SetGrid()
XS100A_Comp.Draw("pe")
int100A_StatC.Draw("pesame")
cXS100A.Update()

####################################################################################
####################################################################################
####################################################################################

## Statistical combination only
int60A_Combo  = int60A_Stat .Clone("int60A_Combo")
inc60A_Combo  = inc60A_Stat .Clone("inc60A_Combo")
int100A_Combo = int100A_Stat.Clone("int100A_Combo")
inc100A_Combo = inc100A_Stat.Clone("inc100A_Combo")


int100A_Combo.Add(int60A_Combo)
inc100A_Combo.Add(inc60A_Combo)

XS_Combo = int100A_Combo.Clone("XS")
XS_Combo.Scale(101.)
XS_Combo.Divide(inc100A_Combo)


## Syst combination only
int60AMax_Combo   = hInteractingKEMax_60A  .Clone("int60A_Max")
inc60AMax_Combo   = hIncidentKEMax_60A     .Clone("inc60A_Max")
int100AMax_Combo  = hInteractingKEMax_100A .Clone("int100A_Max")
inc100AMax_Combo  = hIncidentKEMax_100A    .Clone("inc100A_Max")

int60AMax_Combo.Multiply(pion_Content_Int_60A)
int60AMax_Combo.Divide(eff_Corr_45_Int_60A)
inc60AMax_Combo.Multiply(pion_Content_Inc_60A)
inc60AMax_Combo.Divide(eff_Corr_45_Inc_60A)

int100AMax_Combo.Multiply(pion_Content_Int_100A)
int100AMax_Combo.Divide(eff_Corr_45_Int_100A)
inc100AMax_Combo.Multiply(pion_Content_Inc_100A)
inc100AMax_Combo.Divide(eff_Corr_45_Inc_100A)



int100AMax_Combo.Add(int60AMax_Combo)
inc100AMax_Combo.Add(inc60AMax_Combo)

XSMax_Combo = int100AMax_Combo.Clone("XS")
XSMax_Combo.Scale(101.)
XSMax_Combo.Divide(inc100AMax_Combo)


int60AMin_Combo   = hInteractingKEMin_60A  .Clone("int60A_Min")
inc60AMin_Combo   = hIncidentKEMin_60A     .Clone("inc60A_Min")
int100AMin_Combo  = hInteractingKEMin_100A .Clone("int100A_Min")
inc100AMin_Combo  = hIncidentKEMin_100A    .Clone("inc100A_Min")

int60AMin_Combo.Multiply(pion_Content_Int_60A)
int60AMin_Combo.Divide(eff_Corr_45_Int_60A)
inc60AMin_Combo.Multiply(pion_Content_Inc_60A)
inc60AMin_Combo.Divide(eff_Corr_45_Inc_60A)

int100AMin_Combo.Multiply(pion_Content_Int_100A)
int100AMin_Combo.Divide(eff_Corr_45_Int_100A)
inc100AMin_Combo.Multiply(pion_Content_Inc_100A)
inc100AMin_Combo.Divide(eff_Corr_45_Inc_100A)


int100AMin_Combo.Add(int60AMin_Combo)
inc100AMin_Combo.Add(inc60AMin_Combo)

XSMin_Combo = int100AMin_Combo.Clone("XS")
XSMin_Combo.Scale(101.)
XSMin_Combo.Divide(inc100AMin_Combo)

XSMax_Combo.SetLineColor(kRed)
XSMin_Combo.SetLineColor(kBlue)

cXSAll = TCanvas("cXSAll","cXSAll",600,600)
XS_Combo.Draw("pe")
XSMax_Combo.Draw("pesame")
XSMin_Combo.Draw("pesame")


ComboStatSysHigh, ComboStatSysLow = array( 'd' ), array( 'd' ) 
############################# CALCULATE THIS
for i in xrange(XS_Combo.GetSize()):
    binXSMin          = XSMin_Combo   .GetBinContent(i)
    binXSMax          = XSMax_Combo   .GetBinContent(i)
    binXS             = XS_Combo   .GetBinContent(i)

    xs        = [binXS , binXSMax , binXSMin    ]
    SysHigh   = max(xs)   - binXS
    SysLow    = binXS     - min(xs)
    StatOnly  = XS_Combo.GetBinError(i)
    StatSysHigh = TMath.Sqrt(SysHigh*SysHigh + StatOnly*StatOnly)
    StatSysLow  = TMath.Sqrt(SysLow*SysLow   + StatOnly*StatOnly)

    ComboStatSysHigh.append( StatSysHigh)
    ComboStatSysLow .append( StatSysLow )



cXSHist = TCanvas("cXSHist","cXSHist",1200,600)
cXSHist.Divide(2,1)
p1 = cXSHist.cd(1)
p1.SetGrid()
int100A_Combo.SetLineColor(kRed)
int60A_Stat.SetLineColor(kBlue)
int100A_Stat.SetLineColor(kBlack)

int100A_Combo.SetFillColor(0)
int60A_Stat.SetFillColor(0)
int100A_Stat.SetFillColor(0)

int100A_Combo.Draw("histo")
int60A_Stat.Draw("histosame")
int100A_Stat.Draw("histosame")

p2 = cXSHist.cd(2)
p2.SetGrid()
inc100A_Combo.SetLineColor(kRed)
inc60A_Stat.SetLineColor(kBlue)
inc100A_Stat.SetLineColor(kBlack)

inc100A_Combo.SetFillColor(0)
inc60A_Stat.SetFillColor(0)
inc100A_Stat.SetFillColor(0)

inc100A_Combo.Draw("histo")
inc60A_Stat.Draw("histosame")
inc100A_Stat.Draw("histosame")

cXSHist.Update()



###################################################################################
y_XS  , eyl_XS  , eyh_XS   = array( 'd' ), array( 'd' ), array( 'd' )
x_XS  , exl_XS  , exh_XS   = array( 'd' ), array( 'd' ), array( 'd' )


X100A        = gr100A_Comp.GetX()
Y100A        = gr100A_Comp.GetY()
ErrYHigh100A = gr100A_Comp.GetEYhigh()
ErrYLow100A  = gr100A_Comp.GetEYlow()

X60A        = gr60A_Comp.GetX()
Y60A        = gr60A_Comp.GetY()
ErrYHigh60A = gr60A_Comp.GetEYhigh()
ErrYLow60A  = gr60A_Comp.GetEYlow()

for i in xrange(len(X60A)):
#    print X100A[i], Y100A[i], ErrYHigh100A[i], ErrYLow100A[i]
#    print X60A[i] , Y60A[i] , ErrYHigh60A[i] , ErrYLow60A[i]
#    print XS_Combo.GetBinContent(i)
#    print

    if i < 5:
        x_XS   .append(-100.)
    else:
        x_XS   .append(X60A[i])
    exl_XS .append(25.)
    exh_XS .append(25.)


    y_XS   .append(XS_Combo.GetBinContent(i))
    if Y100A[i] > 0 and Y60A[i] > 0:
        errYHigh = TMath.Sqrt(ErrYHigh100A[i]*ErrYHigh100A[i] + ErrYHigh60A[i]*ErrYHigh60A[i] + ComboStatSysHigh[i]*ComboStatSysHigh[i])
        errYLow  = TMath.Sqrt(ErrYLow100A[i] *ErrYLow100A[i]  + ErrYLow60A[i] *ErrYLow60A[i]  + ComboStatSysLow[i]*ComboStatSysLow[i]  )
        print ErrYLow100A[i], ErrYLow60A[i], ComboStatSysLow[i]
        eyh_XS .append(errYHigh)
        eyl_XS .append(errYLow)
    
    elif Y100A[i] > 0:
        eyl_XS .append(TMath.Sqrt(ErrYLow100A[i]*ErrYLow100A[i]   + ComboStatSysLow[i]  * ComboStatSysLow[i]))
        eyh_XS .append(TMath.Sqrt(ErrYHigh100A[i]*ErrYHigh100A[i] + ComboStatSysHigh[i] * ComboStatSysHigh[i]))

    elif Y60A[i] > 0:
        eyl_XS .append(TMath.Sqrt(ErrYLow60A[i]  * ErrYLow60A[i]   + ComboStatSysLow[i]  * ComboStatSysLow[i]))
        eyh_XS .append(TMath.Sqrt(ErrYHigh60A[i] * ErrYHigh60A[i]  + ComboStatSysHigh[i] * ComboStatSysHigh[i]))

    else:
        eyl_XS .append(0.)
        eyh_XS .append(0.)

for i in xrange(len(X60A)):
    print x_XS[i], exl_XS[i], exh_XS[i], round(y_XS[i],2), round(eyl_XS[i],2), round(eyh_XS[i],2)

###################################################################################

grXS_ComboStatSys   = TGraphAsymmErrors(XS_Combo.GetSize()-2,x_XS, y_XS, exl_XS, exh_XS, ComboStatSysLow, ComboStatSysLow)

grXS_Combo  = TGraphAsymmErrors(XS_Combo.GetSize()-2,x_XS, y_XS, exl_XS, exh_XS, eyl_XS, eyh_XS)
XS_Combo.GetYaxis().SetRangeUser(0,2.5)
XS_Combo.GetXaxis().SetRangeUser(0,1200)


cXSCombined = TCanvas("cXSCombined","cXSCombined",600,600)
cXSCombined.SetGrid()
XS_Combo.Draw("")
grXS_Combo.Draw("P")
XS_Combo.SetLineColor(kRed)
XS100A_Comp.SetLineColor(kRed)
XS60A_Comp.SetLineColor(kRed-2)
#XS100A_Comp.Draw("pesame")
#XS60A_Comp.Draw("pesame")
XS_Combo.Draw("pesame")
cXSCombined.Update()


outFile = TFile("Combined_PlusTable.root","recreate")
outFile.cd()

XS_Combo   .Write("XS_Combined"    ,TObject.kWriteDelete)  
grXS_Combo .Write("XS_Sys_Combined",TObject.kWriteDelete)  
grXS_ComboStatSys .Write("XS_ComboStatSys",TObject.kWriteDelete)  
XSMin_Combo.Write("XSMin_Combo", TObject.kWriteDelete)
XSMax_Combo.Write("XSMax_Combo", TObject.kWriteDelete)

outFile.Write()
outFile.Close()

raw_input()

