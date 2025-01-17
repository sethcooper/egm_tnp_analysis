# ## samples are defined in etc/inputs/tnpSampleDef.py
# ## not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSamplesUL as tnpSamples
#############################################################
# ######### General settings
#############################################################

# flag to be Tested
flags = {
    "passingVeto":    "(passingVeto   == 1)",
    "passingLoose":   "(passingLoose  == 1)",
    "passingMedium":  "(passingMedium == 1)",
    "passingTight":   "(passingTight  == 1)",
    "passingTrigger": "(passHltEle32WPTightGsf == 1) && (passHltEle115CaloIdVTGsfTrkIdTGsf == 1) && (passHltPhoton200 == 1)",
}
baseOutDir = "results/trigger/"

#############################################################
# ######### samples definition  - preparing the samples
#############################################################
tnpTreeDir = "tnpEleTrig"

samplesDef = {
    "data": tnpSamples.UL2018["data_Run2018A"].clone(),
    "mcNom": tnpSamples.UL2018["DY_madgraph"].clone(),
    # "mcAlt": tnpSamples.UL2018["mc_DY_amcatnlo_ele"].clone(),
    "mcAlt": None,
    "tagSel": tnpSamples.UL2018["DY_madgraph"].clone(),
}
# # can add data sample easily
# samplesDef['data'].add_sample( tnpSamples.UL2018['data_2016_runC_ele'] )
# samplesDef['data'].add_sample( tnpSamples.UL2018['data_2016_runD_ele'] )

# # some sample-based cuts... general cuts defined here after
# # require mcTruth on MC DY samples and additional cuts
# # all the samples MUST have different names (i.e. sample.name must be different for all)
# # if you need to use 2 times the same sample, then rename the second one
# samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef["mcNom"] is None:
    samplesDef["mcNom"].set_mcTruth()
if not samplesDef["mcAlt"] is None:
    samplesDef["mcAlt"].set_mcTruth()
if not samplesDef["tagSel"] is None:
    samplesDef["tagSel"].set_mcTruth()
if not samplesDef["tagSel"] is None:
    samplesDef["tagSel"].rename("mcAltSel_DY_madgraph_ele")
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 40')  # FIXME TODO SIC: not sure about this cut value

# # set MC weight, simple way (use tree weight)
weightName = "totWeight"
if not samplesDef["mcNom"] is None:
    samplesDef["mcNom"].set_weight(weightName)
if not samplesDef["mcAlt"] is None:
    samplesDef["mcAlt"].set_weight(weightName)
if not samplesDef["tagSel"] is None:
    samplesDef["tagSel"].set_weight(weightName)

#############################################################
# ######### bining definition  [can be nD bining]
#############################################################
biningDef = [
    {
        "var": "el_sc_eta",
        "type": "float",
        "bins": [-2.5, -1.566, -1.4442, 0.0, 1.4442, 1.566, 2.5],
    },
    {"var": "el_pt", "type": "float", "bins": [50., 60., 100, 200., 500.]},
]

#############################################################
# ######### Cuts definition for all samples
#############################################################
# ## cut
cutBase = "tag_Ele_pt > 35 && passingHEEPV70"

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
# additionalCuts = {
#     0: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     1: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     2: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     3: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     4: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     5: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     6: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     7: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     8: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
#     9: "tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45",
# }

# ### or remove any additional cut (default)
additionalCuts = None

#############################################################
# ######### fitting params to tune fit by hand if necessary
#############################################################
# from Jaesung
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]", "sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]", "sigmaF[0.5,0.1,5.0]",
    "acmsP[60.,50.,80.]", "betaP[0.05,0.01,0.08]", "gammaP[0.1, 0, 1]", "peakP[90.0]",
    "acmsF[60.,50.,80.]", "betaF[0.05,0.01,0.08]", "gammaF[0.1, 0, 1]", "peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]", "sigmaP[1,0.7,6.0]",  "alphaP[2.0,1.2,3.5]", 'nP[3,-5,5]', "sigmaP_2[1.5,0.5,6.0]", "sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]", "sigmaF[2,0.7,15.0]", "alphaF[2.0,1.2,3.5]", 'nF[3,-5,5]', "sigmaF_2[2.0,0.5,6.0]", "sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]", "betaP[0.04,0.01,0.06]", "gammaP[0.1, 0.005, 1]", "peakP[90.0]",
    "acmsF[60.,50.,75.]", "betaF[0.04,0.01,0.06]", "gammaF[0.1, 0.005, 1]", "peakF[90.0]",
    ]

tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]", "sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]", "sigmaF[0.5,0.1,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
