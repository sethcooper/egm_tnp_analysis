from libPython.tnpClassUtils import tnpSample

# eos repositories
eosUL2017 = (
    "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_MINIAOD_Nm1/"
)
eosUL2018 = (
    "/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_MINIAOD_Nm1/"
)
eosUL2016 = (
    "/eos/cms/store/group/phys_egamma/akapoor/Tag-and-Probe_Tree/UL2016_ntuples/"
)


UL2017 = {
    # ## MiniAOD TnP for IDs scale factors
    "DY_madgraph": tnpSample(
        "DY_madgraph", eosUL2017 + "DYJetsToEE.root ", isMC=True, nEvts=-1
    ),
    #    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
    #                                       eosUL2017 + 'DYJetsToLLM50amcatnloFXFX.root',
    #                                       isMC = True, nEvts =  -1 ),
    "DY_amcatnloext": tnpSample(
        "DY_amcatnloext",
        eosUL2017 + "DYJetsToLL_amcatnloFXFX.root",
        isMC=True,
        nEvts=-1,
    ),
    "data_Run2017B": tnpSample(
        "data_Run2017B", eosUL2017 + "SingleEle_RunB.root", lumi=4.793961427
    ),
    "data_Run2017C": tnpSample(
        "data_Run2017C", eosUL2017 + "SingleEle_RunC.root", lumi=9.631214821
    ),
    "data_Run2017D": tnpSample(
        "data_Run2017D", eosUL2017 + "SingleEle_RunD.root", lumi=4.247682053
    ),
    "data_Run2017E": tnpSample(
        "data_Run2017E", eosUL2017 + "SingleEle_RunE.root", lumi=9.313642402
    ),
    "data_Run2017F": tnpSample(
        "data_Run2017F", eosUL2017 + "SingleEle_RunF.root", lumi=13.510934811
    ),
}

UL2018 = {
    # ## MiniAOD TnP for IDs scale factors
    "DY_madgraph": tnpSample(
        "DY_madgraph", "/afs/cern.ch/user/s/scooper/work/private/cmssw/10_6_13/LegacyTriggerScaleFactors/src/EgammaAnalysis/TnPTreeProducer/python/TnPTree_mc.root", isMC=True, nEvts=-1
    ),
    "DY_amcatnloext": tnpSample(
        "DY_amcatnloext",
        eosUL2018 + "DYJetsToLL_amcatnloFXFX.root",
        isMC=True,
        nEvts=-1,
    ),
    "data_Run2018A": tnpSample(
        "data_Run2018A", "/afs/cern.ch/user/s/scooper/work/private/cmssw/10_6_13/LegacyTriggerScaleFactors/src/EgammaAnalysis/TnPTreeProducer/python/TnPTree_data.root", lumi=14.02672485
    ),
    "data_Run2018B": tnpSample(
        "data_Run2018B", eosUL2018 + "EGamma_RunB.root", lumi=7.060617355
    ),
    "data_Run2018C": tnpSample(
        "data_Run2018C", eosUL2018 + "EGamma_RunC.root", lumi=6.894770971
    ),
    "data_Run2018D": tnpSample(
        "data_Run2018D", eosUL2018 + "EGamma_RunD.root", lumi=31.74220577
    ),
}


UL2016_preVFP = {
    # MiniAOD TnP for IDs scale factors
    "DY_madgraph": tnpSample(
        "DY_madgraph",
        eosUL2016
        + "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_preVFP_UL2016.root",
        isMC=True,
        nEvts=-1,
    ),
    "DY_amcatnloext": tnpSample(
        "DY_amcatnloext",
        eosUL2016
        + "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_preVFP_UL2016.root",
        isMC=True,
        nEvts=-1,
    ),
    "data_Run2016B": tnpSample(
        "data_Run2016B", eosUL2016 + "UL2016_SingleEle_Run2016B.root", lumi=0.030493962
    ),
    "data_Run2016B_ver2": tnpSample(
        "data_Run2016B_ver2",
        eosUL2016 + "UL2016_SingleEle_Run2016B_ver2.root",
        lumi=5.879330594,
    ),
    "data_Run2016C": tnpSample(
        "data_Run2016C", eosUL2016 + "UL2016_SingleEle_Run2016C.root", lumi=2.64992914
    ),
    "data_Run2016D": tnpSample(
        "data_Run2016D", eosUL2016 + "UL2016_SingleEle_Run2016D.root", lumi=4.292865604
    ),
    "data_Run2016E": tnpSample(
        "data_Run2016E", eosUL2016 + "UL2016_SingleEle_Run2016E.root", lumi=4.185165152
    ),
    "data_Run2016F": tnpSample(
        "data_Run2016F", eosUL2016 + "UL2016_SingleEle_Run2016F.root", lumi=2.725508364
    ),
}

UL2016_postVFP = {
    # MiniAOD TnP for IDs scale factors
    "DY_madgraph": tnpSample(
        "DY_madgraph",
        eosUL2016
        + "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_postVFP_UL2016.root",
        isMC=True,
        nEvts=-1,
    ),
    "DY_amcatnloext": tnpSample(
        "DY_amcatnloext",
        eosUL2016
        + "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_postVFP_UL2016.root",
        isMC=True,
        nEvts=-1,
    ),
    "data_Run2016F_postVFP": tnpSample(
        "data_Run2016F_postVFP",
        eosUL2016 + "UL2016_SingleEle_Run2016F_postVFP.root",
        lumi=0.414987426,
    ),
    "data_Run2016G": tnpSample(
        "data_Run2016G", eosUL2016 + "UL2016_SingleEle_Run2016G.root", lumi=7.634508755
    ),
    "data_Run2016H": tnpSample(
        "data_Run2016H", eosUL2016 + "UL2016_SingleEle_Run2016H.root", lumi=8.802242522
    ),
}
