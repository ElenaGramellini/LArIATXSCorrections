from ROOT import *
import os
import math
import argparse

gStyle.SetOptStat(0)
# Get BeamComposition: percentage of pions, muons and electrons in a 100A beam configuration


fmuonTwice = TFile.Open("bkgFiles/BkgSub_1.2muons_1.0electrons_100A.root")
fmuonHalf  = TFile.Open("bkgFiles/BkgSub_0.8muons_1.0electrons_100A.root")
felecHalf  = TFile.Open("bkgFiles/BkgSub_1.0muons_0.8electrons_100A.root")
felecTwice = TFile.Open("bkgFiles/BkgSub_1.0muons_1.2electrons_100A.root")
fbasis     = TFile.Open("bkgFiles/BkgSub_1.0muons_1.0electrons_100A.root")


# Interacting and Incident Names
interactingName = "pion_Content_Int_100A"
incidentName    = "pion_Content_Inc_100A"


# Interacting Plot
muonTwice_Int  = fmuonTwice.Get(interactingName)
muonHalf_Int   = fmuonHalf.Get(interactingName)
elecHalf_Int   = felecHalf .Get(interactingName)
elecTwice_Int  = felecTwice.Get(interactingName)
basis_Int      = fbasis    .Get(interactingName)



muonTwice_Int  .SetLineWidth(2)
muonHalf_Int  .SetLineWidth(2)
elecHalf_Int   .SetLineWidth(2)
elecTwice_Int  .SetLineWidth(2)
basis_Int      .SetLineWidth(4)


muonTwice_Int  .SetFillColor(0)
muonHalf_Int   .SetFillColor(0)
elecHalf_Int   .SetFillColor(0)
elecTwice_Int  .SetFillColor(0)
basis_Int      .SetFillColor(0)
basis_Int      .SetMarkerColor(kAzure+6)


muonTwice_Int  .SetLineColor(kBlue)
muonHalf_Int   .SetLineColor(kBlue-2)
elecHalf_Int   .SetLineColor(kRed-2)
elecTwice_Int  .SetLineColor(kRed)
basis_Int      .SetLineColor(kAzure+6)


basis_Int.GetXaxis().SetRangeUser(0,1200.)
basis_Int.GetYaxis().SetRangeUser(0,1.6)
basis_Int.GetYaxis().SetTitleOffset(1.3)

legend = TLegend(.54,.52,.84,.70);
legend.AddEntry(basis_Int,"Estimated #pi content");
legend.AddEntry(muonTwice_Int,"Muons x 1.2");
legend.AddEntry(muonHalf_Int,"Muons x 0.8");
legend.AddEntry(elecTwice_Int,"Electrons x 1.2");
legend.AddEntry(elecHalf_Int,"Electrons x 0.8");




              
c100A_Int_Multiple = TCanvas("c100A_Int_Multiple" ,"XSM Contributions" ,200 ,10 ,1200 ,600)
c100A_Int_Multiple.Divide(2,1)
p1 = c100A_Int_Multiple.cd(1)
p1.SetGrid()

basis_Int.Draw("histo")
muonTwice_Int  .Draw("histosame")
muonHalf_Int  .Draw("histosame")
elecHalf_Int   .Draw("histosame")
elecTwice_Int  .Draw("histosame")

legend.Draw("same")
c100A_Int_Multiple.Update()


c100A_Int_Multiple.cd(2)
p2 = c100A_Int_Multiple.cd(2)
p2.SetGrid()
Systematic_Int = basis_Int.Clone("Systematic_Int")
binValues = []
for i in xrange(basis_Int.GetSize()):
    binValues.append(basis_Int.GetBinContent(i))
    binValues.append(muonTwice_Int.GetBinContent(i))
    binValues.append(muonHalf_Int.GetBinContent(i))
    binValues.append(elecHalf_Int .GetBinContent(i))
    binValues.append(elecTwice_Int.GetBinContent(i))

    maxValue = max(binValues)
    minValue = min(binValues)
    #print minValue, maxValue
    #print binValues

    sysBinValue = (maxValue+minValue)/2.
    sysBinError = (maxValue-minValue)/2.

    #Fix Some representation problem
    if sysBinValue < 0.001:
        sysBinValue = 0
        sysBinError = 0
    Systematic_Int.SetBinContent(i, sysBinValue)
    Systematic_Int.SetBinError(i, sysBinError)

    binValues = []


Systematic_Int.SetLineColor(kAzure-1)
Systematic_Int.SetFillColor(kAzure-1)
Systematic_Int.Draw("pe3")
basis_Int.Draw("pesame")


legend2 = TLegend(.54,.52,.84,.70);
legend2.AddEntry(basis_Int,"#pi Content Interacting, Stat Only");
legend2.AddEntry(Systematic_Int,"#pi Content Interacting, Systematics");
legend2.Draw("same")

c100A_Int_Multiple.Update()

#############################################################################################################
# Incident Plot
muonTwice_Inc  = fmuonTwice.Get(incidentName)
muonHalf_Inc   = fmuonHalf .Get(incidentName)
elecHalf_Inc   = felecHalf .Get(incidentName)
elecTwice_Inc  = felecTwice.Get(incidentName)
basis_Inc      = fbasis    .Get(incidentName)



muonTwice_Inc  .SetLineWidth(2)
muonHalf_Inc   .SetLineWidth(2)
elecHalf_Inc   .SetLineWidth(2)
elecTwice_Inc  .SetLineWidth(2)
basis_Inc      .SetLineWidth(4)


muonTwice_Inc  .SetFillColor(0)
muonHalf_Inc   .SetFillColor(0)
elecHalf_Inc   .SetFillColor(0)
elecTwice_Inc  .SetFillColor(0)
basis_Inc      .SetFillColor(0)
basis_Inc      .SetMarkerColor(kAzure+6)


muonTwice_Inc  .SetLineColor(kBlue)
muonHalf_Inc   .SetLineColor(kBlue-2)
elecHalf_Inc   .SetLineColor(kRed-2)
elecTwice_Inc  .SetLineColor(kRed)
basis_Inc      .SetLineColor(kAzure+6)


basis_Inc.GetXaxis().SetRangeUser(0,1200.)
basis_Inc.GetYaxis().SetRangeUser(0,1.6)
basis_Inc.GetYaxis().SetTitleOffset(1.3)

legend3 = TLegend(.44,.62,.84,.90);
legend3.AddEntry(basis_Inc,"Estimated #pi content");
legend3.AddEntry(muonTwice_Inc,"Muons x 1.2");
legend3.AddEntry(muonHalf_Inc ,"Muons x 0.8");
legend3.AddEntry(elecTwice_Inc,"Electrons x 1.2");
legend3.AddEntry(elecHalf_Inc,"Electrons x 0.8");


              
c100A_Inc_Multiple = TCanvas("c100A_Inc_Multiple" ,"XSM Contributions" ,200 ,10 ,1200 ,600)
c100A_Inc_Multiple.Divide(2,1)
p1 = c100A_Inc_Multiple.cd(1)
p1.SetGrid()

basis_Inc.Draw("histo")
muonTwice_Inc  .Draw("histosame")
muonHalf_Inc   .Draw("histosame")
elecHalf_Inc   .Draw("histosame")
elecTwice_Inc  .Draw("histosame")

legend3.Draw("same")
c100A_Inc_Multiple.Update()


c100A_Inc_Multiple.cd(2)
p2 = c100A_Inc_Multiple.cd(2)
p2.SetGrid()
Systematic_Inc = basis_Inc.Clone("Systematic_Inc")
binValues = []
for i in xrange(basis_Inc.GetSize()):
    binValues.append(basis_Inc.GetBinContent(i))
    binValues.append(muonTwice_Inc.GetBinContent(i))
    binValues.append(muonHalf_Inc.GetBinContent(i))
    binValues.append(elecHalf_Inc .GetBinContent(i))
    binValues.append(elecTwice_Inc.GetBinContent(i))

    maxValue = max(binValues)
    minValue = min(binValues)
    #print minValue, maxValue
    #print binValues

    sysBinValue = (maxValue+minValue)/2.
    sysBinError = (maxValue-minValue)/2.
    
    #Fix Some representation problem
    if sysBinValue < 0.001:
        sysBinValue = 0
        sysBinError = 0

    Systematic_Inc.SetBinContent(i, sysBinValue)
    Systematic_Inc.SetBinError(i, sysBinError)

    binValues = []


Systematic_Inc.SetLineColor(kAzure-1)
Systematic_Inc.SetFillColor(kAzure-1)
Systematic_Inc.Draw("pe3")
basis_Inc.Draw("pesame")

legend4 = TLegend(.44,.62,.84,.90);
legend4.AddEntry(basis_Inc,"#pi Content Incident, Stat Only");
legend4.AddEntry(Systematic_Inc,"#pi Content Incident, Systematics");
legend4.Draw("same")

c100A_Inc_Multiple.Update()


c100A_Multiple = TCanvas("c100A_Multiple" ,"XSM Contributions" ,200 ,10 ,1200 ,600)
c100A_Multiple.Divide(2,1)
pM1 =c100A_Multiple.cd(1) 
pM1.SetGrid()
Systematic_Int.Draw("pe3")
basis_Int.Draw("pesame")
legend2.Draw("same")

pM2 =c100A_Multiple.cd(2) 
pM2.SetGrid()
Systematic_Inc.Draw("pe3")
basis_Inc.Draw("pesame")
legend4.Draw("same")





#########################################
legend9 = TLegend(.44,.72,.90,.90);
legend9.AddEntry(basis_Int,"Estimated #pi content -100A");
legend9.AddEntry(muonTwice_Int,"Muons x 1.2");
legend9.AddEntry(muonHalf_Int,"Muons x 0.8");
legend9.AddEntry(elecTwice_Int,"Electrons x 1.2");
legend9.AddEntry(elecHalf_Int,"Electrons x 0.8");

basis_Int.SetTitle("Background Correction, Interacting; Kinetic Energy [MeV];C^{#pi MC}_{Interacting}")
basis_Inc.SetTitle("Background Correction, Incident; Kinetic Energy [MeV];C^{#pi MC}_{Incident}")

for i in xrange(5):
    basis_Int      .SetBinContent(i,0)
    muonTwice_Int  .SetBinContent(i,0)
    muonHalf_Int   .SetBinContent(i,0)
    elecHalf_Int   .SetBinContent(i,0)
    elecTwice_Int  .SetBinContent(i,0)
    basis_Inc      .SetBinContent(i,0)
    muonTwice_Inc  .SetBinContent(i,0)
    muonHalf_Inc  .SetBinContent(i,0)
    elecHalf_Inc   .SetBinContent(i,0)
    elecTwice_Inc  .SetBinContent(i,0)
    basis_Int      .SetBinError(i,0)
    muonTwice_Int  .SetBinError(i,0)
    muonHalf_Int   .SetBinError(i,0)
    elecHalf_Int   .SetBinError(i,0)
    elecTwice_Int  .SetBinError(i,0)
    basis_Inc      .SetBinError(i,0)
    muonTwice_Inc  .SetBinError(i,0)
    muonHalf_Inc  .SetBinError(i,0)
    elecHalf_Inc   .SetBinError(i,0)
    elecTwice_Inc  .SetBinError(i,0)


for i in xrange(24,30):
    basis_Int      .SetBinContent(i,0)
    muonTwice_Int  .SetBinContent(i,0)
    muonHalf_Int   .SetBinContent(i,0)
    elecHalf_Int   .SetBinContent(i,0)
    elecTwice_Int  .SetBinContent(i,0)
    basis_Inc      .SetBinContent(i,0)
    muonTwice_Inc  .SetBinContent(i,0)
    muonHalf_Inc  .SetBinContent(i,0)
    elecHalf_Inc   .SetBinContent(i,0)
    elecTwice_Inc  .SetBinContent(i,0)
    basis_Int      .SetBinError(i,0)
    muonTwice_Int  .SetBinError(i,0)
    muonHalf_Int   .SetBinError(i,0)
    elecHalf_Int   .SetBinError(i,0)
    elecTwice_Int  .SetBinError(i,0)
    basis_Inc      .SetBinError(i,0)
    muonTwice_Inc  .SetBinError(i,0)
    muonHalf_Inc  .SetBinError(i,0)
    elecHalf_Inc   .SetBinError(i,0)
    elecTwice_Inc  .SetBinError(i,0)


c100A_Int2_Multiple = TCanvas("c100A_Int2_Multiple" ,"XSM Contributions" ,200 ,10 ,1200 ,600)
c100A_Int2_Multiple.Divide(2,1)
p1 = c100A_Int2_Multiple.cd(1)
p1.SetGrid()
basis_Int.Draw("][histo")
muonTwice_Int  .Draw("][histosame")
muonHalf_Int  .Draw("][histosame")
elecHalf_Int   .Draw("][histosame")
elecTwice_Int  .Draw("][histosame")
legend9.Draw("same")
p2 = c100A_Int2_Multiple.cd(2)
p2.SetGrid()
basis_Inc.Draw("][histo")
muonTwice_Inc  .Draw("][histosame")
muonHalf_Inc  .Draw("][histosame")
elecHalf_Inc   .Draw("][histosame")
elecTwice_Inc  .Draw("][histosame")
legend9.Draw("same")

c100A_Int2_Multiple.Update()

c100A_Int2_Multiple.SaveAs("Bkg100A_inc_int.pdf")


raw_input()  



