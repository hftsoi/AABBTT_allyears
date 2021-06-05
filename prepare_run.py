import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sample', '-s', default=None, help='Output name')
parser.add_argument('--channel', '-c', default=None, help='Output name')
parser.add_argument('--year', '-y', default=None, help='Output name')

args = parser.parse_args()

if __name__ == "__main__":

    place=""
    datatype=""
    name=[]

    ###################################################
    # 2018 data 
    ###################################################
    if args.year=="2018" and args.sample=="data" and args.channel=="mt":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_data/"
       datatype="data"
       name=[
"data_SingleMuon_Run2018A-17Sep2018","DataA","0","2018",
"data_SingleMuon_Run2018B-17Sep2018","DataB","0","2018",
"data_SingleMuon_Run2018C-17Sep2018","DataC","0","2018",
"data_SingleMuon_Run2018D-PromptReco","DataD","0","2018"
]
    if args.year=="2018" and args.sample=="data" and args.channel=="et":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_data/"
       datatype="data"
       name=[
"data_EGamma_Run2018A-17Sep2018","DataA","0","2018",
"data_EGamma_Run2018B-17Sep2018","DataB","0","2018",
"data_EGamma_Run2018C-17Sep2018","DataC","0","2018",
"data_EGamma_Run2018D-PromptReco","DataD","0","2018"
]
    if args.year=="2018" and args.sample=="data" and args.channel=="em":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_data/"
       datatype="data"
       name=[
"data_MuonEG_Run2018A-17Sep2018","DataA","0","2018",
"data_MuonEG_Run2018B-17Sep2018","DataB","0","2018",
"data_MuonEG_Run2018C-17Sep2018","DataC","0","2018",
"data_MuonEG_Run2018D-PromptReco","DataD","0","2018"
]
    if args.year=="2018" and args.sample=="data" and args.channel=="tt":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_data/"
       datatype="data"
       name=[
"data_Tau_Run2018A-17Sep2018","DataA","0","2018",
"data_Tau_Run2018B-17Sep2018","DataB","0","2018",
"data_Tau_Run2018C-17Sep2018","DataC","0","2018",
"data_Tau_Run2018D-PromptReco","DataD","0","2018"
]

    if args.year=="2018" and args.sample=="data" and (args.channel=="emm" or args.channel=="mmt" or args.channel=="mtt"):
       place="/hdfs/store/user/caillol/LTT_2018_7sep_data/"
       datatype="data"
       name=[
"data_SingleMuon_Run2018A-17Sep2018","DataA","0","2018",
"data_SingleMuon_Run2018B-17Sep2018","DataB","0","2018",
"data_SingleMuon_Run2018C-17Sep2018","DataC","0","2018",
"data_SingleMuon_Run2018D-PromptReco","DataD","0","2018"
]

    if args.year=="2018" and args.sample=="data" and (args.channel=="eet" or args.channel=="eem" or args.channel=="ett"):
       place="/hdfs/store/user/caillol/LTT_2018_7sep_data/"
       datatype="data"
       name=[
"data_EGamma_Run2018A-17Sep2018","SingleEleA","0","2018",
"data_EGamma_Run2018B-17Sep2018","SingleEleB","0","2018",
"data_EGamma_Run2018C-17Sep2018","SingleEleC","0","2018",
"data_EGamma_Run2018D-PromptReco","SingleEleD","0","2018"
]

    if args.year=="2018" and args.sample=="data" and (args.channel=="emt"):
       place="/hdfs/store/user/caillol/LTT_2018_7sep_data/"
       datatype="data"
       name=[
"data_SingleMuon_Run2018A-17Sep2018","SingleMuA","0","2018",
"data_SingleMuon_Run2018B-17Sep2018","SingleMuB","0","2018",
"data_SingleMuon_Run2018C-17Sep2018","SingleMuC","0","2018",
"data_SingleMuon_Run2018D-PromptReco","SingleMuD","0","2018",
"data_EGamma_Run2018A-17Sep2018","SingleEleA","0","2018",
"data_EGamma_Run2018B-17Sep2018","SingleEleB","0","2018",
"data_EGamma_Run2018C-17Sep2018","SingleEleC","0","2018",
"data_EGamma_Run2018D-PromptReco","SingleEleD","0","2018"
]

    if args.year=="2018" and args.sample=="data" and (args.channel=="mmem" or args.channel=="mmet" or args.channel=="mmmt" or args.channel=="mmtt"):
       place="/hdfs/store/user/caillol/LLTT_2018_7sep_data/"
       datatype="data"
       name=[
"data_SingleMuon_Run2018A-17Sep2018","SingleMuA","0","2018",
"data_SingleMuon_Run2018B-17Sep2018","SingleMuB","0","2018",
"data_SingleMuon_Run2018C-17Sep2018","SingleMuC","0","2018",
"data_SingleMuon_Run2018D-PromptReco","SingleMuD","0","2018"
]

    if args.year=="2018" and args.sample=="data" and (args.channel=="eeem" or args.channel=="eeet" or args.channel=="eemt" or args.channel=="eett"):
       place="/hdfs/store/user/caillol/LLTT_2018_7sep_data/"
       datatype="data"
       name=[
"data_EGamma_Run2018A-17Sep2018","SingleEleA","0","2018",
"data_EGamma_Run2018B-17Sep2018","SingleEleB","0","2018",
"data_EGamma_Run2018C-17Sep2018","SingleEleC","0","2018",
"data_EGamma_Run2018D-PromptReco","SingleEleD","0","2018"
]

    ##############################################################
    # 2018 Embedded
    ##############################################################
    if args.sample=="embedded" and args.year=="2018" and args.channel=="em":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_embedded/"
       datatype="embedded"
       name=[
"embedded_EmbeddingRun2018A_ElMuFinalState","EmbeddedA","0","2018",
"embedded_EmbeddingRun2018B_ElMuFinalState","EmbeddedB","0","2018",
"embedded_EmbeddingRun2018C_ElMuFinalState","EmbeddedC","0","2018",
"embedded_EmbeddingRun2018D_ElMuFinalState","EmbeddedD","0","2018"
]

    if args.sample=="embedded" and args.year=="2018" and args.channel=="et":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_embedded/"
       datatype="embedded"
       name=[
"embedded_EmbeddingRun2018A_ElTauFinalState","EmbeddedA","0","2018",
"embedded_EmbeddingRun2018B_ElTauFinalState","EmbeddedB","0","2018",
"embedded_EmbeddingRun2018C_ElTauFinalState","EmbeddedC","0","2018",
"embedded_EmbeddingRun2018D_ElTauFinalState","EmbeddedD","0","2018"
]

    if args.sample=="embedded" and args.year=="2018" and args.channel=="mt":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_embedded/"
       datatype="embedded"
       name=[
"embedded_EmbeddingRun2018A_MuTauFinalState","EmbeddedA","0","2018",
"embedded_EmbeddingRun2018B_MuTauFinalState","EmbeddedB","0","2018",
"embedded_EmbeddingRun2018C_MuTauFinalState","EmbeddedC","0","2018",
"embedded_EmbeddingRun2018D_MuTauFinalState","EmbeddedD","0","2018"
]

    if args.sample=="embedded" and args.year=="2018" and args.channel=="tt":
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018_embedded/"
       datatype="embedded"
       name=[
"embedded_EmbeddingRun2018A_TauTauFinalState","EmbeddedA","0","2018",
"embedded_EmbeddingRun2018B_TauTauFinalState","EmbeddedB","0","2018",
"embedded_EmbeddingRun2018C_TauTauFinalState","EmbeddedC","0","2018",
"embedded_EmbeddingRun2018D_TauTauFinalState","EmbeddedD","0","2018"
]

###########################  2018 MC  ############################

    if args.year=="2018" and args.sample=="mc" and (args.channel=="eeem" or args.channel=="eeet" or args.channel=="eemt" or args.channel=="eett" or args.channel=="mmem" or args.channel=="mmet" or args.channel=="mmmt" or args.channel=="mmtt"):
       place="/hdfs/store/user/caillol/LLTT_2018_7sep/"
       datatype="mc"
       name=[
"GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","GGHWW","0","2018",
"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v3","GGZZ2e2mu","0","2018",
"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v3","GGZZ2e2tau","0","2018",
"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v4","GGZZ2mu2tau","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4e_v1","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4e_v2","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","GGZZ4e_v3","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4mu_v1","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4mu_v2","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","GGZZ4mu_v3","0","2018",
"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4tau_v1","0","2018",
"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4tau_v2","0","2018",
"GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_-102X_upgrade2018_realistic_v15-v1","GGZHWW","0","2018",
"HWminusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WminusHWW","0","2018",
"HWplusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WplusHWW","0","2018",
"HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","ZHWW","0","2018",
"VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","VBFHWW","0","2018",
"WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WWW","0","2018",
"WWZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WWZ","0","2018",
"WZTo3LNu_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WZ3LNu","0","2018",
"WZZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WZZ","0","2018",
"WminusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WminusHTT","0","2018",
"WplusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WplusHTT","0","2018",
"ZHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","ZHTT","0","2018",
"ZZTo4L_TuneCP5_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ZZ4L_v1","0","2018",
"ZZTo4L_TuneCP5_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext2-v2","ZZ4L_v2","0","2018",
"ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ZZZ","0","2018",
"ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHLLTT","0","2018",
"ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHNNTT","0","2018",
"ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHQQTT","0","2018",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v2","ttHnonbb","0","2018",
"ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","ttHTT","0","2018",
"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ttW","0","2018",
"ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ttZ","0","2018",
"SUSYZHToAA_AToBB_AToTauTau_M-40_FilterTauTauReco_TuneCP5_13TeV_madgraph_pythia8","zh_bbtt40","0","2018"
]

    if args.year=="2018" and args.sample=="mc" and (args.channel=="eem" or args.channel=="eet" or args.channel=="emt" or args.channel=="emm" or args.channel=="mmt" or args.channel=="mtt" or args.channel=="ett"):
       place="/hdfs/store/user/caillol/LTT_2018_7sep/"
       datatype="mc"
       name=[
"GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","GGHWW","0","2018",
"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v3","GGZZ2e2mu","0","2018",
"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v3","GGZZ2e2tau","0","2018",
"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v4","GGZZ2mu2tau","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4e_v1","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4e_v2","0","2018",
"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","GGZZ4e_v3","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4mu_v1","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4mu_v2","0","2018",
"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","GGZZ4mu_v3","0","2018",
"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZZ4tau_v1","0","2018",
"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_-102X_upgrade2018_realistic_v15-v2","GGZZ4tau_v2","0","2018",
"GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_-102X_upgrade2018_realistic_v15-v1","GGZHWW","0","2018",
"HWminusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WminusHWW","0","2018",
"HWplusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WplusHWW","0","2018",
"HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","ZHWW","0","2018",
"VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","VBFHWW","0","2018",
"WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WWW","0","2018",
"WWZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WWZ","0","2018",
"WZTo3LNu_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WZ3LNu","0","2018",
"WZZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WZZ","0","2018",
"WminusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WminusHTT","0","2018",
"WplusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WplusHTT","0","2018",
"ZHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","ZHTT","0","2018",
"ZZTo4L_TuneCP5_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ZZ4L_v1","0","2018",
"ZZTo4L_TuneCP5_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext2-v2","ZZ4L_v2","0","2018",
"ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ZZZ","0","2018",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v2","ttHnonbb","0","2018",
"ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","ttHTT","0","2018",
"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ttW","0","2018",
"ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","ttZ","0","2018",
"SUSYWHToAA_AToBB_AToTauTau_M-40_FilterTauTauReco_TuneCP5_13TeV_madgraph_pythia8","wh_bbtt40","0","2018"
]

    if args.sample=="signal" and args.year=="2018" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018/"
      datatype="mc"
      name=[
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt12","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt15","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt20","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt25","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt30","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt35","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v2","ggH_bbtt40_v1","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v3","ggH_bbtt40_v2","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt45","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt50","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt55","Z","2018",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","ggH_bbtt60","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt12","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt15","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt20","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt25","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt30","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt35","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt40","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v2","vbf_bbtt45_v1","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v4","vbf_bbtt45_v2","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v5","vbf_bbtt45_v3","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v4","vbf_bbtt50","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt55","Z","2018",
"SUSYVBFHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_-102X_upgrade2018_realistic_v15-v1","vbf_bbtt60","Z","2018"
]

    if args.year=="2018" and args.sample=="mc" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
       place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2018/"
       datatype="mc"
       name=[
"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","DYlow_v1","Z","2018",
"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","DYlow_v2","Z","2018",
"DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","DY1_v1","Z","2018",
"DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","DY1_v2","Z","2018",
"DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","DY2_v1","Z","2018",
"DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","DY2_v2","Z","2018",
"DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","DY3_v1","Z","2018",
"DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","DY3_v2","Z","2018",
"DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","DY4","Z","2018",
"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","DY","Z","2018",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","GGHTT","0","2018",
"GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","GGHWW","0","2018",
"GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_-102X_upgrade2018_realistic_v15-v1","GGZHWW","0","2018",
"HWminusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WminusHWW","0","2018",
"HWplusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","WplusHWW","0","2018",
"HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5_-102X_upgrade2018_realistic_v15-v1","ZHWW","0","2018",
"ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_-102X_upgrade2018_realistic_v15-v1","ST_t_antitop","0","2018",
"ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","ST_t_top","0","2018",
"ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","ST_tW_antitop","0","2018",
"ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","ST_tW_top","0","2018",
"TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","TTTo2L2Nu","0","2018",
"TTToHadronic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","TTToHadronic_v1","0","2018",
"TTToHadronic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext2-v2","TTToHadronic_v2","0","2018",
"TTToHadronic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext2-v3","TTToHadronic_v3","0","2018",
"TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v1","TTToSemiLeptonic_v1","0","2018",
"TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext3-v2","TTToSemiLeptonic_v2","0","2018",
"TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15_ext3-v3","TTToSemiLeptonic_v3","0","2018",
"VBFHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15_ext1-v1","VBFHTT","0","2018",
"VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_-102X_upgrade2018_realistic_v15-v1","VBFHWW","0","2018",
"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_-102X_upgrade2018_realistic_v15-v1","VV2L2Nu","0","2018",
"W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","W1","W","2018",
"W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","W2_v1","W","2018",
"W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","W2_v2","W","2018",
"W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","W3_v1","W","2018",
"W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","W3_v2","W","2018",
"W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v1","W4_v1","W","2018",
"W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","W4_v2","W","2018",
"WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_-102X_upgrade2018_realistic_v15-v2","W","W","2018",
"WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_-102X_upgrade2018_realistic_v15-v1","WZ2L2Q","0","2018",
"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_-102X_upgrade2018_realistic_v15-v1","WZ3LNu_v1","0","2018",
"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_-102X_upgrade2018_realistic_v15_ext1-v2","WZ3LNu_v2","0","2018",
"WminusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WminusHTT","0","2018",
"WplusHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","WplusHTT","0","2018",
"ZHToTauTau_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v2","ZHTT","0","2018",
"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_-102X_upgrade2018_realistic_v15-v1","ZZ2L2Q","0","2018",
"ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8_-102X_upgrade2018_realistic_v15-v1","ZZ4L","0","2018",
"ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHLLTT","0","2018",
"ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHNNTT","0","2018",
"ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8_-102X_upgrade2018_realistic_v15-v1","GGZHQQTT","0","2018",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v2","ttHnonbb","0","2018",
"ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v2","ttHbb_v1","0","2018",
"ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_-102X_upgrade2018_realistic_v15-v3","ttHbb_v2","0","2018"
]

    #####################################################################
    # 2017 Data 
    #####################################################################
    if args.sample=="data" and args.year=="2017" and args.channel=="em":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_data/"
      datatype="data"
      name=[
"data_MuonEG_Run2017B-31Mar2018","DataB","0","2017",
"data_MuonEG_Run2017C-31Mar2018","DataC","0","2017",
"data_MuonEG_Run2017D-31Mar2018","DataD","0","2017",
"data_MuonEG_Run2017E-31Mar2018","DataE","0","2017",
"data_MuonEG_Run2017F-31Mar2018","DataF","0","2017"
]

    if args.sample=="data" and args.year=="2017" and args.channel=="et":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_data/"
      datatype="data"
      name=[
"data_SingleElectron_Run2017B-31Mar2018","DataB","0","2017",
"data_SingleElectron_Run2017C-31Mar2018","DataC","0","2017",
"data_SingleElectron_Run2017D-31Mar2018","DataD","0","2017",
"data_SingleElectron_Run2017E-31Mar2018","DataE","0","2017",
"data_SingleElectron_Run2017F-31Mar2018","DataF","0","2017"
]

    if args.sample=="data" and args.year=="2017" and args.channel=="mt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_data/"
      datatype="data"
      name=[
"data_SingleMuon_Run2017B-31Mar2018","DataB","0","2017",
"data_SingleMuon_Run2017C-31Mar2018","DataC","0","2017",
"data_SingleMuon_Run2017D-31Mar2018","DataD","0","2017",
"data_SingleMuon_Run2017E-31Mar2018","DataE","0","2017",
"data_SingleMuon_Run2017F-31Mar2018","DataF","0","2017"
]

    if args.sample=="data" and args.year=="2017" and args.channel=="tt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_data/"
      datatype="data"
      name=[
"data_Tau_Run2017B-31Mar2018","DataB","0","2017",
"data_Tau_Run2017C-31Mar2018","DataC","0","2017",
"data_Tau_Run2017D-31Mar2018","DataD","0","2017",
"data_Tau_Run2017E-31Mar2018","DataE","0","2017",
"data_Tau_Run2017F-31Mar2018","DataF","0","2017"
]

    #####################################################################
    # 2017 Embedded 
    #####################################################################

    if args.sample=="embedded" and args.year=="2017" and args.channel=="em":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2017B_ElMuFinalState","embeddedB","0","2017",
"embedded_EmbeddingRun2017C_ElMuFinalState","embeddedC","0","2017",
"embedded_EmbeddingRun2017D_ElMuFinalState","embeddedD","0","2017",
"embedded_EmbeddingRun2017E_ElMuFinalState","embeddedE","0","2017",
"embedded_EmbeddingRun2017F_ElMuFinalState","embeddedF","0","2017"
]

    if args.sample=="embedded" and args.year=="2017" and args.channel=="et":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2017B_ElTauFinalState","embeddedB","0","2017",
"embedded_EmbeddingRun2017C_ElTauFinalState","embeddedC","0","2017",
"embedded_EmbeddingRun2017D_ElTauFinalState","embeddedD","0","2017",
"embedded_EmbeddingRun2017E_ElTauFinalState","embeddedE","0","2017",
"embedded_EmbeddingRun2017F_ElTauFinalState","embeddedF","0","2017"
]

    if args.sample=="embedded" and args.year=="2017" and args.channel=="mt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2017B_MuTauFinalState","embeddedB","0","2017",
"embedded_EmbeddingRun2017C_MuTauFinalState","embeddedC","0","2017",
"embedded_EmbeddingRun2017D_MuTauFinalState","embeddedD","0","2017",
"embedded_EmbeddingRun2017E_MuTauFinalState","embeddedE","0","2017",
"embedded_EmbeddingRun2017F_MuTauFinalState","embeddedF","0","2017"
]

    if args.sample=="embedded" and args.year=="2017" and args.channel=="tt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2017B_TauTauFinalState","embeddedB","0","2017",
"embedded_EmbeddingRun2017C_TauTauFinalState","embeddedC","0","2017",
"embedded_EmbeddingRun2017D_TauTauFinalState","embeddedD","0","2017",
"embedded_EmbeddingRun2017E_TauTauFinalState","embeddedE","0","2017",
"embedded_EmbeddingRun2017F_TauTauFinalState","embeddedF","0","2017"
]

    #####################################################################
    # 2017 MC 
    #####################################################################
    if args.sample=="mc" and args.year=="2017" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017/"
      datatype="mc"
      name=[
"DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1","DY1_v1","Z","2017",
"DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","DY1_v2","Z","2017",
"DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_v3_94X_mc2017_realistic_v14_ext1-v2","DY1_v3","Z","2017",
"DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","DY2_v1","Z","2017",
"DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1","DY2_v2","Z","2017",
"DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2","DY2_v3","Z","2017",
"DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","DY3_v1","Z","2017",
"DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1","DY3_v2","Z","2017",
"DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v2","DY3_v3","Z","2017",
"DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","DY4_v1","Z","2017",
"DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_v2_94X_mc2017_realistic_v14-v2","DY4_v2","Z","2017",
"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","DYlow_v1","Z","2017",
"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2","DYlow_v2","Z","2017",
"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2","DYlow_v3","Z","2017",
"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1","DY_v1","Z","2017",
"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1","DY_v2","Z","2017",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","GGHTT_v1","Z","2017",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1","GGHTT_v2","Z","2017",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2","GGHTT_v3","Z","2017",
"GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","GGHWW","Z","2017",
"GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","GGZHWW","0","2017",
"HWminusJ_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WminusHWW","0","2017",
"HWplusJ_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WplusHWW","0","2017",
"HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4","ZHWW","0","2017",
"ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ST_t_antitop_v1","0","2017",
"ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2","ST_t_antitop_v2","0","2017",
"ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ST_t_top_v1","0","2017",
"ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","ST_t_top_v2","0","2017",
"ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ST_tW_antitop_v1","0","2017",
"ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2","ST_tW_antitop_v2","0","2017",
"ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ST_tW_top_v1","0","2017",
"ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2","ST_tW_top_v2","0","2017",
"TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","TTTo2L2Nu","0","2017",
"TTToHadronic_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2","TTToHadronic","0","2017",
"TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","TTToSemiLeptonic","0","2017",
"VBFHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","VBFHTT_v1","Z","2017",
"VBFHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","VBFHTT_v2","Z","2017",
"VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","VBFHWW","Z","2017",
"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","VVTo2L2Nu","0","2017",
"W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3","W1_v1","W","2017",
"W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4","W1_v2","W","2017",
"W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4","W2_v1","W","2017",
"W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5","W2_v2","W","2017",
"W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","W3_v1","W","2017",
"W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_PU2017_94X_mc2017_realistic_v14-v1","W3_v2","W","2017",
"W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","W4_v1","W","2017",
"W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2","W4_v2","W","2017",
"WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2","W_v1","W","2017",
"WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3","W_v2","W","2017",
"WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2","W_v3","W","2017",
"WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WZ2L2Q","0","2017",
"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WZ3L1Nu_v1","0","2017",
"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","WZ3L1Nu_v2","0","2017",
"WminusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WminusHTT","0","2017",
"WplusHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","WplusHTT","0","2017",
"ZHToTauTau_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ZHTT","0","2017",
"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ZZ2L2Q","0","2017",
"ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ZZ4L","0","2017",
"ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","GGZHLLTT","0","2017",
"ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","GGZHNNTT","0","2017",
"ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2","GGZHQQTT","0","2017",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ttHnonbb_v1","0","2017",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2","ttHnonbb_v2","0","2017",
"ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","ttHnonbb_v3","0","2017",
"ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ttHbb_v1","0","2017",
"ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_v2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1","ttHbb_v2","0","2017"
]

    if args.sample=="signal" and args.year=="2017" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2017/"
      datatype="mc"
      name=[
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt12","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt15","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt20","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt25","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt30","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt35","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt40","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt45","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt50","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt55","Z","2017",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","ggH_bbtt60","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt12","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt15","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt20","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt25","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt30","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt35","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt40","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt45","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt50","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt55","Z","2017",
"SUSYVBFHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8_v2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1","vbf_bbtt60","Z","2017"
]



    ######################################################################
    # 2016 data 
    ######################################################################

    if args.sample=="data" and args.year=="2016" and args.channel=="em":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_data/"
      datatype="data"
      name=[
"data_MuonEG_Run2016B_v1","DataBv1","0","2016",
"data_MuonEG_Run2016B_v2","DataBv2","0","2016",
"data_MuonEG_Run2016C","DataC","0","2016",
"data_MuonEG_Run2016D","DataD","0","2016",
"data_MuonEG_Run2016E","DataE","0","2016",
"data_MuonEG_Run2016F","DataF","0","2016",
"data_MuonEG_Run2016G","DataG","0","2016",
"data_MuonEG_Run2016H","DataH","0","2016"
]

    if args.sample=="data" and args.year=="2016" and args.channel=="et":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_data/"
      datatype="data"
      name=[
"data_SingleElectron_Run2016B_v1","DataBv1","0","2016",
"data_SingleElectron_Run2016B_v2","DataBv2","0","2016",
"data_SingleElectron_Run2016C","DataC","0","2016",
"data_SingleElectron_Run2016D","DataD","0","2016",
"data_SingleElectron_Run2016E","DataE","0","2016",
"data_SingleElectron_Run2016F","DataF","0","2016",
"data_SingleElectron_Run2016G","DataG","0","2016",
"data_SingleElectron_Run2016H","DataH","0","2016"
]

    if args.sample=="data" and args.year=="2016" and args.channel=="mt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_data/"
      datatype="data"
      name=[
"data_SingleMuon_Run2016B_v1","DataBv1","0","2016",
"data_SingleMuon_Run2016B_v2","DataBv2","0","2016",
"data_SingleMuon_Run2016C","DataC","0","2016",
"data_SingleMuon_Run2016D","DataD","0","2016",
"data_SingleMuon_Run2016E","DataE","0","2016",
"data_SingleMuon_Run2016F","DataF","0","2016",
"data_SingleMuon_Run2016G","DataG","0","2016",
"data_SingleMuon_Run2016H","DataH","0","2016"
]

    if args.sample=="data" and args.year=="2016" and args.channel=="tt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_data/"
      datatype="data"
      name=[
"data_Tau_Run2016B_v1","DataBv1","0","2016",
"data_Tau_Run2016B_v2","DataBv2","0","2016",
"data_Tau_Run2016C","DataC","0","2016",
"data_Tau_Run2016D","DataD","0","2016",
"data_Tau_Run2016E","DataE","0","2016",
"data_Tau_Run2016F","DataF","0","2016",
"data_Tau_Run2016G","DataG","0","2016",
"data_Tau_Run2016H","DataH","0","2016"
]

    ##################################################
    # 2016 Embedded 
    ##################################################

    if args.sample=="embedded" and args.year=="2016" and args.channel=="em":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2016B_ElMuFinalState","embeddedB","0","2016",
"embedded_EmbeddingRun2016C_ElMuFinalState","embeddedC","0","2016",
"embedded_EmbeddingRun2016D_ElMuFinalState","embeddedD","0","2016",
"embedded_EmbeddingRun2016E_ElMuFinalState","embeddedE","0","2016",
"embedded_EmbeddingRun2016F_ElMuFinalState","embeddedF","0","2016",
"embedded_EmbeddingRun2016G_ElMuFinalState","embeddedG","0","2016",
"embedded_EmbeddingRun2016H_ElMuFinalState","embeddedH","0","2016"
]

    if args.sample=="embedded" and args.year=="2016" and args.channel=="et":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2016B_ElTauFinalState","embeddedB","0","2016",
"embedded_EmbeddingRun2016C_ElTauFinalState","embeddedC","0","2016",
"embedded_EmbeddingRun2016D_ElTauFinalState","embeddedD","0","2016",
"embedded_EmbeddingRun2016E_ElTauFinalState","embeddedE","0","2016",
"embedded_EmbeddingRun2016F_ElTauFinalState","embeddedF","0","2016",
"embedded_EmbeddingRun2016G_ElTauFinalState","embeddedG","0","2016",
"embedded_EmbeddingRun2016H_ElTauFinalState","embeddedH","0","2016"
]

    if args.sample=="embedded" and args.year=="2016" and args.channel=="mt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2016B_MuTauFinalState","embeddedB","0","2016",
"embedded_EmbeddingRun2016C_MuTauFinalState","embeddedC","0","2016",
"embedded_EmbeddingRun2016D_MuTauFinalState","embeddedD","0","2016",
"embedded_EmbeddingRun2016E_MuTauFinalState","embeddedE","0","2016",
"embedded_EmbeddingRun2016F_MuTauFinalState","embeddedF","0","2016",
"embedded_EmbeddingRun2016G_MuTauFinalState","embeddedG","0","2016",
"embedded_EmbeddingRun2016H_MuTauFinalState","embeddedH","0","2016"
]

    if args.sample=="embedded" and args.year=="2016" and args.channel=="tt":
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016_embedded/"
      datatype="embedded"
      name=[
"embedded_EmbeddingRun2016B_TauTauFinalState","embeddedB","0","2016",
"embedded_EmbeddingRun2016C_TauTauFinalState","embeddedC","0","2016",
"embedded_EmbeddingRun2016D_TauTauFinalState","embeddedD","0","2016",
"embedded_EmbeddingRun2016E_TauTauFinalState","embeddedE","0","2016",
"embedded_EmbeddingRun2016F_TauTauFinalState","embeddedF","0","2016",
"embedded_EmbeddingRun2016G_TauTauFinalState","embeddedG","0","2016",
"embedded_EmbeddingRun2016H_TauTauFinalState","embeddedH","0","2016"
]

    #######################################################################
    # 2016 MC
    #######################################################################

    if args.sample=="signal" and args.year=="2016" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016/"
      datatype="mc"
      name=[
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt15","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt15","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt20","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt20","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt25","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt25","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt30","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt30","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt35","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt35","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt40","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt40","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt45","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-45_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt45","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt50","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt50","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt55","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt55","Z","2016",
"SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","ggH_bbtt60","Z","2016",
"SUSYVBFToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger16_TuneCP5_13TeV_madgraph_pythia8","vbf_bbtt60","Z","2016"
]

    if args.sample=="mc" and args.year=="2016" and (args.channel=="em" or args.channel=="et" or args.channel=="mt" or args.channel=="tt"):
      place="/hdfs/store/user/caillol/HAABBTT_rerunBtag_2016/"
      datatype="mc"
      name=[
"DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY1low","Z","2016",
"DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY2low","Z","2016",
"DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY3low","Z","2016",
"DY4JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY4low","Z","2016",
"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DYlow","Z","2016",
"DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","DY1","Z","2016",
"DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY2","Z","2016",
"DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY3","Z","2016",
"DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","DY4","Z","2016",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","DY_v1","Z","2016",
"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2","DY_v2","Z","2016",
"W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","W1","W","2016",
"W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","W2_v1","W","2016",
"W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","W2_v2","W","2016",
"W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","W3_v1","W","2016",
"W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","W3_v2","W","2016",
"W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","W4_v1","W","2016",
"W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","W4_v2","W","2016",
"W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1","W4_v3","W","2016",
"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","W_v1","W","2016",
"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2","W_v2","W","2016",
"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","ST_t_antitop","0","2016",
"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","ST_t_top","0","2016",
"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1","ST_tW_antitop","0","2016",
"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1","ST_tW_top","0","2016",
"TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","TTTo2L2Nu","0","2016",
"TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","TTToHadronic","0","2016",
"TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","TTToSemiLeptonic","0","2016",
"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","VV2L2Nu_v1","0","2016",
"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","VV2L2Nu_v2","0","2016",
"WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WZ2L2Q","0","2016",
"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WZ3L1Nu","0","2016",
"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","ZZ2L2Q","0","2016",
"ZZTo4L_13TeV-amcatnloFXFX-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2","ZZ4L","0","2016",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","GGHTT_v1","Z","2016",
"GluGluHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3","GGHTT_v2","Z","2016",
"GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","GGHWW","Z","2016",
"GluGluZH_HToWW_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","GGZHWW","0","2016",
"HWminusJ_HToWW_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WminusHWW","0","2016",
"HWplusJ_HToWW_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WplusHWW","0","2016",
"HZJ_HToWW_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","ZHWW","0","2016",
"VBFHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","VBFHTT","Z","2016",
"VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","VBFHWW","Z","2016",
"WminusHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WminusHTT","0","2016",
"WplusHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","WplusHTT","0","2016",
"ZHToTauTau_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","ZHTT","0","2016",
"ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","GGZHLLTT","0","2016",
"ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","GGZHNNTT","0","2016",
"ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","GGZHQQTT","0","2016",
"ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2","ttHnonbb","0","2016",
"ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_v3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1","ttHbb","0","2016"
]

    datadir="/nfs_scratch/htsoi/haabbtt_"+args.channel+args.year+"_rerunBtag/"
    all_File = open("do_submit_"+args.sample+"_"+args.channel+args.year+".sh" , 'w')
    line=""
    line+="mkdir -p "+datadir+ "\n"
    for j in range(0,len(name)/4):
       print name[4*j],name[4*j+1],name[4*j+2]
       submit_File = open("Submit_"+name[4*j+1]+"_"+datatype+"_"+args.channel+args.year+".sh" , 'w')
       line+="mkdir -p "+datadir+"Out_"+name[4*j+1]+"\n"
       line+="sh Submit_"+name[4*j+1]+"_"+datatype+"_"+args.channel+args.year+".sh" +"\n"
       f=os.popen("ls -t " + place+name[4*j] + "/make* | sort")
       command1=""
       ligne=0
       for i in f.readlines():
	   command1=command1+"./skim_"+args.channel+".exe "+datatype+" "+datadir+"Out_"+name[4*j+1]+"/"+name[4*j+1]+str(ligne)+".root " + i[0:-1] + " " + name[4*j+2] + " " + name[4*j+3] + "\n"
           ligne=ligne+1
       submit_File.write(command1)
       submit_File.close()
    all_File.write(line)
    all_File.close()

