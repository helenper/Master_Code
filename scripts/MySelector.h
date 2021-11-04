//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Jan 17 14:07:49 2019 by ROOT version 6.14/04
// from TTree diboson_NoSys/diboson_NoSys
// found on file: diboson_merged_processed.root
//////////////////////////////////////////////////////////

#ifndef MySelector_h
#define MySelector_h

//ROOT included automaticly
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

// Headers needed by this particular selector - C++
#include <vector>
#include <TH1.h>
#include <TH2.h>




class MySelector : public TSelector {

  private:

  //==================================================
  //
  // Variables for cutflow and counting
  //
  //==================================================

    int n_events_processed; // Variable used to give feedback about progress

    int nPassedSF; 
    int nPassedOC;
    int nPassedjets;
    int nPassedmll;
    int nPassedmetEt; 
    int nPassedmetSign;

    vector<TString> cut_list;
    map<TString, map<TString, float>> eventCount; 



  
  //==================================================
  //
  // Variables handeling input
  //
  //==================================================

    vector<TString> info;
    int info_size; 
    TString inputType;
    TString background_elm;
    TString data_name;
    TString signal_samp;
    TString my_string;
    TString timestamp;
    TString saving_path;
    TString timeperiod;
    TString iso_point;
    TString fake_samp;

  //==================================================
  //
  // Variables used in processing and scaling
  //
  //==================================================

    double luminosity;
    double weights;

  //==================================================
  //
  // Boolean expressions and strings  used in defining cuts 
  // and regions 
  //
  //==================================================
    
    bool SF_basic;
    bool SF_ee_basic;
    bool SF_mumu_basic;
    bool SF_rm_Z;
    bool SF_basic_met_sign;

    bool DF_basic; 

    bool SR_SF_0J; 
    bool SR_SF_1J;
    bool SR_DF_0J; 
    bool SR_DF_1J;
    bool DF_0J; 
    bool DF_1J;

 
    bool cuts; 

    TString cut_string;


 //==================================================
  //
  // Initialize values used for cuts
  //
  //==================================================

    double mll_greater_than;  
    int lep_pt_greater_than;
    int met_greater_than;
    int met_sign_greater_than;
    int dist_from_Z; 
    int ZeroWantedLightJets_def; 
    int OneWantedLightJets_def;

    int nJet;
    int nJetLight;
    int nJetB;

    int nLepSignal;
    int nLepBase;
    vector<int> lepIndex; 

    int Lidx1;
    int Lidx2;

    double mT2;

  //==================================================
  //
  // Histograms and related stuff
  //
  //==================================================

    map<TString, TH1F *> histogram;
    map<TString, TH2D *> histogram2D;
    vector<TString> variables;
    vector<TString> regions;
    vector<TString> h_extra;
    vector<TString> myString;


  //==================================================
  //
  // For logfile
  //
  //==================================================

    string line;



  //==================================================
  //
  // For period 15-16, 17, 18 for data, MC and fakes
  // Comment out last 4 variables when run not for fakes 
  // 
  // 15 Feb 2020
  //
  //==================================================  

public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrig = {fReader, "trigMatch_1L2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_1LTrig = {fReader, "trigMatch_1LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrigOR = {fReader, "trigMatch_1L2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_1LTrigOR = {fReader, "trigMatch_1LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrig = {fReader, "trigMatch_2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrigOR = {fReader, "trigMatch_2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_L1EM20VH = {fReader, "trigMatch_HLT_e24_lhmedium_L1EM20VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_lhmedium = {fReader, "trigMatch_HLT_e60_lhmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e120_lhloose = {fReader, "trigMatch_HLT_e120_lhloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu20_iloose_L1MU15 = {fReader, "trigMatch_HLT_mu20_iloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e12_lhloose_L12EM10VH = {fReader, "trigMatch_HLT_2e12_lhloose_L12EM10VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu18_mu8noL1 = {fReader, "trigMatch_HLT_mu18_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e17_lhloose_mu14 = {fReader, "trigMatch_HLT_e17_lhloose_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e7_lhmedium_mu24 = {fReader, "trigMatch_HLT_e7_lhmedium_mu24"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhtight_nod0_ivarloose = {fReader, "trigMatch_HLT_e24_lhtight_nod0_ivarloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_nod0_L1EM20VH = {fReader, "trigMatch_HLT_e24_lhmedium_nod0_L1EM20VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_medium = {fReader, "trigMatch_HLT_e60_medium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu40 = {fReader, "trigMatch_HLT_mu40"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_iloose_L1MU15 = {fReader, "trigMatch_HLT_mu24_iloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_ivarloose_L1MU15 = {fReader, "trigMatch_HLT_mu24_ivarloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_ivarmedium = {fReader, "trigMatch_HLT_mu24_ivarmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_imedium = {fReader, "trigMatch_HLT_mu24_imedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu26_imedium = {fReader, "trigMatch_HLT_mu26_imedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e15_lhvloose_nod0_L12EM13VH = {fReader, "trigMatch_HLT_2e15_lhvloose_nod0_L12EM13VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e17_lhvloose_nod0 = {fReader, "trigMatch_HLT_2e17_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2mu10 = {fReader, "trigMatch_HLT_2mu10"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2mu14 = {fReader, "trigMatch_HLT_2mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu20_mu8noL1 = {fReader, "trigMatch_HLT_mu20_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu22_mu8noL1 = {fReader, "trigMatch_HLT_mu22_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_nod0_L1EM20VHI_mu8noL1 = {fReader, "trigMatch_HLT_e24_lhmedium_nod0_L1EM20VHI_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhtight_nod0_ivarloose = {fReader, "trigMatch_HLT_e26_lhtight_nod0_ivarloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhtight_nod0 = {fReader, "trigMatch_HLT_e26_lhtight_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_lhmedium_nod0 = {fReader, "trigMatch_HLT_e60_lhmedium_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e140_lhloose_nod0 = {fReader, "trigMatch_HLT_e140_lhloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e300_etcut = {fReader, "trigMatch_HLT_e300_etcut"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu26_ivarmedium = {fReader, "trigMatch_HLT_mu26_ivarmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu50 = {fReader, "trigMatch_HLT_mu50"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu60_0eta105_msonly = {fReader, "trigMatch_HLT_mu60_0eta105_msonly"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e17_lhvloose_nod0_L12EM15VHI = {fReader, "trigMatch_HLT_2e17_lhvloose_nod0_L12EM15VHI"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e24_lhvloose_nod0 = {fReader, "trigMatch_HLT_2e24_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e17_lhloose_nod0_mu14 = {fReader, "trigMatch_HLT_e17_lhloose_nod0_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhmedium_nod0_mu8noL1 = {fReader, "trigMatch_HLT_e26_lhmedium_nod0_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e7_lhmedium_nod0_mu24 = {fReader, "trigMatch_HLT_e7_lhmedium_nod0_mu24"};
   TTreeReaderValue<Float_t> mu = {fReader, "mu"};
   TTreeReaderValue<Float_t> avg_mu = {fReader, "avg_mu"};
   TTreeReaderValue<Float_t> actual_mu = {fReader, "actual_mu"};
   TTreeReaderValue<Int_t> nVtx = {fReader, "nVtx"};
   TTreeReaderValue<Int_t> channel = {fReader, "channel"};
   TTreeReaderValue<Int_t> nLep_base = {fReader, "nLep_base"};
   TTreeReaderValue<Int_t> nLep_signal = {fReader, "nLep_signal"};
   TTreeReaderArray<int> lepFlavor = {fReader, "lepFlavor"};
   TTreeReaderArray<int> lepCharge = {fReader, "lepCharge"};
   TTreeReaderArray<int> lepAuthor = {fReader, "lepAuthor"};
   TTreeReaderArray<float> lepPt = {fReader, "lepPt"};
   TTreeReaderArray<float> lepEta = {fReader, "lepEta"};
   TTreeReaderArray<float> lepPhi = {fReader, "lepPhi"};
   TTreeReaderArray<float> lepM = {fReader, "lepM"};
   TTreeReaderArray<float> lepD0 = {fReader, "lepD0"};
   TTreeReaderArray<float> lepD0Sig = {fReader, "lepD0Sig"};
   TTreeReaderArray<float> lepZ0 = {fReader, "lepZ0"};
   TTreeReaderArray<float> lepZ0SinTheta = {fReader, "lepZ0SinTheta"};
   TTreeReaderArray<float> lepTopoetcone20 = {fReader, "lepTopoetcone20"};
   TTreeReaderArray<float> lepTopoetcone30 = {fReader, "lepTopoetcone30"};
   TTreeReaderArray<float> lepPtvarcone20 = {fReader, "lepPtvarcone20"};
   TTreeReaderArray<float> lepPtvarcone30 = {fReader, "lepPtvarcone30"};
   TTreeReaderArray<float> lepCorrTopoetcone20 = {fReader, "lepCorrTopoetcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone20 = {fReader, "lepCorrPtvarcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone30 = {fReader, "lepCorrPtvarcone30"};
   TTreeReaderValue<vector<bool>> lepPassOR = {fReader, "lepPassOR"};
   TTreeReaderArray<int> lepType = {fReader, "lepType"};
   TTreeReaderArray<int> lepOrigin = {fReader, "lepOrigin"};
   TTreeReaderArray<int> lepEgMotherType = {fReader, "lepEgMotherType"};
   TTreeReaderArray<int> lepEgMotherOrigin = {fReader, "lepEgMotherOrigin"};
   TTreeReaderArray<int> lepEgMotherPdgId = {fReader, "lepEgMotherPdgId"};
   TTreeReaderArray<int> lepECIDS = {fReader, "lepECIDS"};
   TTreeReaderValue<vector<bool>> lepIsHF = {fReader, "lepIsHF"};
   TTreeReaderValue<vector<bool>> lepIsLF = {fReader, "lepIsLF"};
   TTreeReaderValue<vector<bool>> lepIsCO = {fReader, "lepIsCO"};
   TTreeReaderValue<vector<bool>> lepIsCF = {fReader, "lepIsCF"};
   TTreeReaderValue<vector<bool>> lepIsUK = {fReader, "lepIsUK"};
   TTreeReaderValue<vector<bool>> lepIsPR = {fReader, "lepIsPR"};
   TTreeReaderValue<vector<bool>> lepPassBL = {fReader, "lepPassBL"};
   TTreeReaderValue<vector<bool>> lepVeryLoose = {fReader, "lepVeryLoose"};
   TTreeReaderValue<vector<bool>> lepLoose = {fReader, "lepLoose"};
   TTreeReaderValue<vector<bool>> lepMedium = {fReader, "lepMedium"};
   TTreeReaderValue<vector<bool>> lepTight = {fReader, "lepTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCHighPtCaloOnly = {fReader, "lepIsoFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoFixedCutHighPtTrackOnly = {fReader, "lepIsoFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoGradient = {fReader, "lepIsoGradient"};
   TTreeReaderValue<vector<bool>> lepIsoFCLoose = {fReader, "lepIsoFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoFCTight = {fReader, "lepIsoFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCTightTrackOnly = {fReader, "lepIsoFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCHighPtCaloOnly = {fReader, "lepIsoCorrFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFixedCutHighPtTrackOnly = {fReader, "lepIsoCorrFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrGradient = {fReader, "lepIsoCorrGradient"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCLoose = {fReader, "lepIsoCorrFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTight = {fReader, "lepIsoCorrFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTightTrackOnly = {fReader, "lepIsoCorrFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepTruthMatched = {fReader, "lepTruthMatched"};
   TTreeReaderArray<int> lepTruthCharge = {fReader, "lepTruthCharge"};
   TTreeReaderArray<float> lepTruthPt = {fReader, "lepTruthPt"};
   TTreeReaderArray<float> lepTruthEta = {fReader, "lepTruthEta"};
   TTreeReaderArray<float> lepTruthPhi = {fReader, "lepTruthPhi"};
   TTreeReaderArray<float> lepTruthM = {fReader, "lepTruthM"};
   TTreeReaderValue<Int_t> nJet30 = {fReader, "nJet30"};
   TTreeReaderValue<Int_t> nJet20 = {fReader, "nJet20"};
   TTreeReaderValue<Int_t> nBJet20_MV2c10_FixedCutBEff_77 = {fReader, "nBJet20_MV2c10_FixedCutBEff_77"};
   TTreeReaderArray<float> jetPt = {fReader, "jetPt"};
   TTreeReaderArray<float> jetEta = {fReader, "jetEta"};
   TTreeReaderArray<float> jetPhi = {fReader, "jetPhi"};
   TTreeReaderArray<float> jetM = {fReader, "jetM"};
   TTreeReaderArray<float> jetJVT = {fReader, "jetJVT"};
   TTreeReaderValue<vector<bool>> jetPassOR = {fReader, "jetPassOR"};
   TTreeReaderValue<vector<bool>> jetSignal = {fReader, "jetSignal"};
   TTreeReaderValue<Float_t> mjj = {fReader, "mjj"};
   TTreeReaderArray<float> jetTileEnergy = {fReader, "jetTileEnergy"};
   TTreeReaderArray<float> jetMV2c10 = {fReader, "jetMV2c10"};
   TTreeReaderValue<Float_t> met_Et = {fReader, "met_Et"};
   TTreeReaderValue<Float_t> met_Sign = {fReader, "met_Sign"};
   TTreeReaderValue<Float_t> met_Phi = {fReader, "met_Phi"};
   TTreeReaderValue<Float_t> met_Et_loose = {fReader, "met_Et_loose"};
   TTreeReaderValue<Float_t> met_Et_tighter = {fReader, "met_Et_tighter"};
   TTreeReaderValue<Float_t> met_Et_tenacious = {fReader, "met_Et_tenacious"};
   TTreeReaderValue<Float_t> met_Phi_loose = {fReader, "met_Phi_loose"};
   TTreeReaderValue<Float_t> met_Phi_tighter = {fReader, "met_Phi_tighter"};
   TTreeReaderValue<Float_t> met_Phi_tenacious = {fReader, "met_Phi_tenacious"};
   TTreeReaderValue<Float_t> mll = {fReader, "mll"};
   TTreeReaderValue<Double_t> pileupWeight = {fReader, "pileupWeight"};
   TTreeReaderValue<Double_t> leptonWeight = {fReader, "leptonWeight"};
   TTreeReaderValue<Double_t> eventWeight = {fReader, "eventWeight"};
   TTreeReaderValue<Double_t> bTagWeight = {fReader, "bTagWeight"};
   TTreeReaderValue<Double_t> jvtWeight = {fReader, "jvtWeight"};
   TTreeReaderValue<Double_t> globalDiLepTrigSF = {fReader, "globalDiLepTrigSF"};
   TTreeReaderValue<Double_t> flavSymWeight = {fReader, "flavSymWeight"};
   TTreeReaderValue<Double_t> genWeight = {fReader, "genWeight"};
   TTreeReaderValue<Double_t> genWeightUp = {fReader, "genWeightUp"};
   TTreeReaderValue<Double_t> genWeightDown = {fReader, "genWeightDown"};
   TTreeReaderValue<ULong64_t> PRWHash = {fReader, "PRWHash"};
   TTreeReaderValue<ULong64_t> EventNumber = {fReader, "EventNumber"};
   TTreeReaderValue<Float_t> xsec = {fReader, "xsec"};
   TTreeReaderValue<Float_t> GenHt = {fReader, "GenHt"};
   TTreeReaderValue<Float_t> GenMET = {fReader, "GenMET"};
   TTreeReaderValue<Int_t> DatasetNumber = {fReader, "DatasetNumber"};
   TTreeReaderValue<Int_t> RunNumber = {fReader, "RunNumber"};
   TTreeReaderValue<Int_t> RandomRunNumber = {fReader, "RandomRunNumber"};
   TTreeReaderValue<Int_t> FS = {fReader, "FS"};
   // /*
   TTreeReaderArray<double> MM_weight = {fReader, "MM_weight"};
   TTreeReaderArray<double> syst_MM_down = {fReader, "syst_MM_down"};
   TTreeReaderArray<double> syst_MM_up = {fReader, "syst_MM_up"};
   TTreeReaderArray<TString> MM_key = {fReader, "MM_key"};

   //  */




  //==================================================
  //
  // For old n-tuples: period 15-16,17,18 signal, data and MC
  //
  //==================================================  

    /*
 public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrig = {fReader, "trigMatch_1L2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_1LTrig = {fReader, "trigMatch_1LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrigOR = {fReader, "trigMatch_1L2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_1LTrigOR = {fReader, "trigMatch_1LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrig = {fReader, "trigMatch_2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrigOR = {fReader, "trigMatch_2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_L1EM20VH = {fReader, "trigMatch_HLT_e24_lhmedium_L1EM20VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_lhmedium = {fReader, "trigMatch_HLT_e60_lhmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e120_lhloose = {fReader, "trigMatch_HLT_e120_lhloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu20_iloose_L1MU15 = {fReader, "trigMatch_HLT_mu20_iloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e12_lhloose_L12EM10VH = {fReader, "trigMatch_HLT_2e12_lhloose_L12EM10VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu18_mu8noL1 = {fReader, "trigMatch_HLT_mu18_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e17_lhloose_mu14 = {fReader, "trigMatch_HLT_e17_lhloose_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e7_lhmedium_mu24 = {fReader, "trigMatch_HLT_e7_lhmedium_mu24"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhtight_nod0_ivarloose = {fReader, "trigMatch_HLT_e24_lhtight_nod0_ivarloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_nod0_L1EM20VH = {fReader, "trigMatch_HLT_e24_lhmedium_nod0_L1EM20VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_medium = {fReader, "trigMatch_HLT_e60_medium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu40 = {fReader, "trigMatch_HLT_mu40"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_iloose_L1MU15 = {fReader, "trigMatch_HLT_mu24_iloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_ivarloose_L1MU15 = {fReader, "trigMatch_HLT_mu24_ivarloose_L1MU15"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_ivarmedium = {fReader, "trigMatch_HLT_mu24_ivarmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu24_imedium = {fReader, "trigMatch_HLT_mu24_imedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu26_imedium = {fReader, "trigMatch_HLT_mu26_imedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e15_lhvloose_nod0_L12EM13VH = {fReader, "trigMatch_HLT_2e15_lhvloose_nod0_L12EM13VH"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e17_lhvloose_nod0 = {fReader, "trigMatch_HLT_2e17_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2mu10 = {fReader, "trigMatch_HLT_2mu10"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2mu14 = {fReader, "trigMatch_HLT_2mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu20_mu8noL1 = {fReader, "trigMatch_HLT_mu20_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu22_mu8noL1 = {fReader, "trigMatch_HLT_mu22_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e24_lhmedium_nod0_L1EM20VHI_mu8noL1 = {fReader, "trigMatch_HLT_e24_lhmedium_nod0_L1EM20VHI_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhtight_nod0_ivarloose = {fReader, "trigMatch_HLT_e26_lhtight_nod0_ivarloose"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhtight_nod0 = {fReader, "trigMatch_HLT_e26_lhtight_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e60_lhmedium_nod0 = {fReader, "trigMatch_HLT_e60_lhmedium_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e140_lhloose_nod0 = {fReader, "trigMatch_HLT_e140_lhloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e300_etcut = {fReader, "trigMatch_HLT_e300_etcut"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu26_ivarmedium = {fReader, "trigMatch_HLT_mu26_ivarmedium"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu50 = {fReader, "trigMatch_HLT_mu50"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_mu60_0eta105_msonly = {fReader, "trigMatch_HLT_mu60_0eta105_msonly"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e17_lhvloose_nod0_L12EM15VHI = {fReader, "trigMatch_HLT_2e17_lhvloose_nod0_L12EM15VHI"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_2e24_lhvloose_nod0 = {fReader, "trigMatch_HLT_2e24_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e17_lhloose_nod0_mu14 = {fReader, "trigMatch_HLT_e17_lhloose_nod0_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e26_lhmedium_nod0_mu8noL1 = {fReader, "trigMatch_HLT_e26_lhmedium_nod0_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_HLT_e7_lhmedium_nod0_mu24 = {fReader, "trigMatch_HLT_e7_lhmedium_nod0_mu24"};
   TTreeReaderValue<Float_t> mu = {fReader, "mu"};
   TTreeReaderValue<Float_t> avg_mu = {fReader, "avg_mu"};
   TTreeReaderValue<Float_t> actual_mu = {fReader, "actual_mu"};
   TTreeReaderValue<Int_t> nVtx = {fReader, "nVtx"};
   TTreeReaderValue<Int_t> channel = {fReader, "channel"};
   TTreeReaderValue<Int_t> nLep_base = {fReader, "nLep_base"};
   TTreeReaderValue<Int_t> nLep_signal = {fReader, "nLep_signal"};
   TTreeReaderArray<int> lepFlavor = {fReader, "lepFlavor"};
   TTreeReaderArray<int> lepCharge = {fReader, "lepCharge"};
   TTreeReaderArray<int> lepAuthor = {fReader, "lepAuthor"};
   TTreeReaderArray<float> lepPt = {fReader, "lepPt"};
   TTreeReaderArray<float> lepEta = {fReader, "lepEta"};
   TTreeReaderArray<float> lepPhi = {fReader, "lepPhi"};
   TTreeReaderArray<float> lepM = {fReader, "lepM"};
   TTreeReaderArray<float> lepD0 = {fReader, "lepD0"};
   TTreeReaderArray<float> lepD0Sig = {fReader, "lepD0Sig"};
   TTreeReaderArray<float> lepZ0 = {fReader, "lepZ0"};
   TTreeReaderArray<float> lepZ0SinTheta = {fReader, "lepZ0SinTheta"};
   TTreeReaderArray<float> lepTopoetcone20 = {fReader, "lepTopoetcone20"};
   TTreeReaderArray<float> lepTopoetcone30 = {fReader, "lepTopoetcone30"};
   TTreeReaderArray<float> lepPtvarcone20 = {fReader, "lepPtvarcone20"};
   TTreeReaderArray<float> lepPtvarcone30 = {fReader, "lepPtvarcone30"};
   TTreeReaderArray<float> lepCorrTopoetcone20 = {fReader, "lepCorrTopoetcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone20 = {fReader, "lepCorrPtvarcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone30 = {fReader, "lepCorrPtvarcone30"};
   TTreeReaderValue<vector<bool>> lepPassOR = {fReader, "lepPassOR"};
   TTreeReaderArray<int> lepType = {fReader, "lepType"};
   TTreeReaderArray<int> lepOrigin = {fReader, "lepOrigin"};
   TTreeReaderArray<int> lepEgMotherType = {fReader, "lepEgMotherType"};
   TTreeReaderArray<int> lepEgMotherOrigin = {fReader, "lepEgMotherOrigin"};
   TTreeReaderArray<int> lepEgMotherPdgId = {fReader, "lepEgMotherPdgId"};
   TTreeReaderArray<int> lepECIDS = {fReader, "lepECIDS"};
   TTreeReaderValue<vector<bool>> lepIsHF = {fReader, "lepIsHF"};
   TTreeReaderValue<vector<bool>> lepIsLF = {fReader, "lepIsLF"};
   TTreeReaderValue<vector<bool>> lepIsCO = {fReader, "lepIsCO"};
   TTreeReaderValue<vector<bool>> lepIsCF = {fReader, "lepIsCF"};
   TTreeReaderValue<vector<bool>> lepIsUK = {fReader, "lepIsUK"};
   TTreeReaderValue<vector<bool>> lepIsPR = {fReader, "lepIsPR"};
   TTreeReaderValue<vector<bool>> lepPassBL = {fReader, "lepPassBL"};
   TTreeReaderValue<vector<bool>> lepVeryLoose = {fReader, "lepVeryLoose"};
   TTreeReaderValue<vector<bool>> lepLoose = {fReader, "lepLoose"};
   TTreeReaderValue<vector<bool>> lepMedium = {fReader, "lepMedium"};
   TTreeReaderValue<vector<bool>> lepTight = {fReader, "lepTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCHighPtCaloOnly = {fReader, "lepIsoFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoFixedCutHighPtTrackOnly = {fReader, "lepIsoFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoGradient = {fReader, "lepIsoGradient"};
   TTreeReaderValue<vector<bool>> lepIsoFCLoose = {fReader, "lepIsoFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoFCTight = {fReader, "lepIsoFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCTightTrackOnly = {fReader, "lepIsoFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCHighPtCaloOnly = {fReader, "lepIsoCorrFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFixedCutHighPtTrackOnly = {fReader, "lepIsoCorrFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrGradient = {fReader, "lepIsoCorrGradient"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCLoose = {fReader, "lepIsoCorrFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTight = {fReader, "lepIsoCorrFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTightTrackOnly = {fReader, "lepIsoCorrFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepTruthMatched = {fReader, "lepTruthMatched"};
   TTreeReaderArray<int> lepTruthCharge = {fReader, "lepTruthCharge"};
   TTreeReaderArray<float> lepTruthPt = {fReader, "lepTruthPt"};
   TTreeReaderArray<float> lepTruthEta = {fReader, "lepTruthEta"};
   TTreeReaderArray<float> lepTruthPhi = {fReader, "lepTruthPhi"};
   TTreeReaderArray<float> lepTruthM = {fReader, "lepTruthM"};
   TTreeReaderValue<Int_t> nJet30 = {fReader, "nJet30"};
   TTreeReaderValue<Int_t> nJet20 = {fReader, "nJet20"};
   TTreeReaderValue<Int_t> nBJet20_MV2c10_FixedCutBEff_77 = {fReader, "nBJet20_MV2c10_FixedCutBEff_77"};
   TTreeReaderArray<float> jetPt = {fReader, "jetPt"};
   TTreeReaderArray<float> jetEta = {fReader, "jetEta"};
   TTreeReaderArray<float> jetPhi = {fReader, "jetPhi"};
   TTreeReaderArray<float> jetM = {fReader, "jetM"};
   TTreeReaderArray<float> jetJVT = {fReader, "jetJVT"};
   TTreeReaderValue<vector<bool>> jetPassOR = {fReader, "jetPassOR"};
   TTreeReaderValue<vector<bool>> jetSignal = {fReader, "jetSignal"};
   TTreeReaderValue<Float_t> mjj = {fReader, "mjj"};
   TTreeReaderArray<float> jetTileEnergy = {fReader, "jetTileEnergy"};
   TTreeReaderArray<float> jetMV2c10 = {fReader, "jetMV2c10"};
   TTreeReaderValue<Float_t> met_Et = {fReader, "met_Et"};
   TTreeReaderValue<Float_t> met_Sign = {fReader, "met_Sign"};
   TTreeReaderValue<Float_t> met_Phi = {fReader, "met_Phi"};
   TTreeReaderValue<Float_t> met_Et_loose = {fReader, "met_Et_loose"};
   TTreeReaderValue<Float_t> met_Et_tighter = {fReader, "met_Et_tighter"};
   TTreeReaderValue<Float_t> met_Et_tenacious = {fReader, "met_Et_tenacious"};
   TTreeReaderValue<Float_t> met_Phi_loose = {fReader, "met_Phi_loose"};
   TTreeReaderValue<Float_t> met_Phi_tighter = {fReader, "met_Phi_tighter"};
   TTreeReaderValue<Float_t> met_Phi_tenacious = {fReader, "met_Phi_tenacious"};
   TTreeReaderValue<Float_t> mll = {fReader, "mll"};
   TTreeReaderValue<Double_t> pileupWeight = {fReader, "pileupWeight"};
   TTreeReaderValue<Double_t> leptonWeight = {fReader, "leptonWeight"};
   TTreeReaderValue<Double_t> eventWeight = {fReader, "eventWeight"};
   TTreeReaderValue<Double_t> bTagWeight = {fReader, "bTagWeight"};
   TTreeReaderValue<Double_t> jvtWeight = {fReader, "jvtWeight"};
   TTreeReaderValue<Double_t> globalDiLepTrigSF = {fReader, "globalDiLepTrigSF"};
   TTreeReaderValue<Double_t> flavSymWeight = {fReader, "flavSymWeight"};
   TTreeReaderValue<Double_t> genWeight = {fReader, "genWeight"};
   TTreeReaderValue<Double_t> genWeightUp = {fReader, "genWeightUp"};
   TTreeReaderValue<Double_t> genWeightDown = {fReader, "genWeightDown"};
   TTreeReaderValue<ULong64_t> PRWHash = {fReader, "PRWHash"};
   TTreeReaderValue<ULong64_t> EventNumber = {fReader, "EventNumber"};
   TTreeReaderValue<Float_t> xsec = {fReader, "xsec"};
   TTreeReaderValue<Float_t> GenHt = {fReader, "GenHt"};
   TTreeReaderValue<Float_t> GenMET = {fReader, "GenMET"};
   TTreeReaderValue<Int_t> DatasetNumber = {fReader, "DatasetNumber"};
   TTreeReaderValue<Int_t> RunNumber = {fReader, "RunNumber"};
   TTreeReaderValue<Int_t> RandomRunNumber = {fReader, "RandomRunNumber"};
   TTreeReaderValue<Int_t> FS = {fReader, "FS"};

   // */


  //==================================================
  //
  // For old n-tuples: data15-16 and mc16a
  //
  //==================================================  
    /*
  public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrig = {fReader, "trigMatch_1L2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_1L2LTrigOR = {fReader, "trigMatch_1L2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrig = {fReader, "trigMatch_2LTrig"};
   TTreeReaderValue<Bool_t> trigMatch_2LTrigOR = {fReader, "trigMatch_2LTrigOR"};
   TTreeReaderValue<Bool_t> trigMatch_2e12_lhloose_L12EM10VH = {fReader, "trigMatch_2e12_lhloose_L12EM10VH"};
   TTreeReaderValue<Bool_t> trigMatch_e17_lhloose_mu14 = {fReader, "trigMatch_e17_lhloose_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_2mu10 = {fReader, "trigMatch_2mu10"};
   TTreeReaderValue<Bool_t> trigMatch_2e17_lhvloose_nod0 = {fReader, "trigMatch_2e17_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_e17_lhloose_nod0_mu14 = {fReader, "trigMatch_e17_lhloose_nod0_mu14"};
   TTreeReaderValue<Bool_t> trigMatch_e7_lhmedium_nod0_mu24 = {fReader, "trigMatch_e7_lhmedium_nod0_mu24"};
   TTreeReaderValue<Bool_t> trigMatch_mu22_mu8noL1 = {fReader, "trigMatch_mu22_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_2mu14 = {fReader, "trigMatch_2mu14"};
   TTreeReaderValue<Bool_t> trigMatch_2e24_lhvloose_nod0 = {fReader, "trigMatch_2e24_lhvloose_nod0"};
   TTreeReaderValue<Bool_t> trigMatch_mu24_mu8noL1 = {fReader, "trigMatch_mu24_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_mu20_mu8noL1 = {fReader, "trigMatch_mu20_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_mu18_mu8noL1 = {fReader, "trigMatch_mu18_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_2e15_lhvloose_nod0_L12EM13VH = {fReader, "trigMatch_2e15_lhvloose_nod0_L12EM13VH"};
   TTreeReaderValue<Bool_t> trigMatch_2e17_lhvloose_nod0_L12EM15VHI = {fReader, "trigMatch_2e17_lhvloose_nod0_L12EM15VHI"};
   TTreeReaderValue<Bool_t> trigMatch_e26_lhmedium_nod0_mu8noL1 = {fReader, "trigMatch_e26_lhmedium_nod0_mu8noL1"};
   TTreeReaderValue<Bool_t> trigMatch_e24_lhmedium_nod0_L1EM20VHI_mu8noL1 = {fReader, "trigMatch_e24_lhmedium_nod0_L1EM20VHI_mu8noL1"};
   TTreeReaderValue<Float_t> mu = {fReader, "mu"};
   TTreeReaderValue<Float_t> avg_mu = {fReader, "avg_mu"};
   TTreeReaderValue<Float_t> actual_mu = {fReader, "actual_mu"};
   TTreeReaderValue<Int_t> nVtx = {fReader, "nVtx"};
   TTreeReaderValue<Int_t> channel = {fReader, "channel"};
   TTreeReaderValue<Int_t> nLep_base = {fReader, "nLep_base"};
   TTreeReaderValue<Int_t> nLep_signal = {fReader, "nLep_signal"};
   TTreeReaderArray<int> lepFlavor = {fReader, "lepFlavor"};
   TTreeReaderArray<int> lepCharge = {fReader, "lepCharge"};
   TTreeReaderArray<int> lepAuthor = {fReader, "lepAuthor"};
   TTreeReaderArray<float> lepPt = {fReader, "lepPt"};
   TTreeReaderArray<float> lepEta = {fReader, "lepEta"};
   TTreeReaderArray<float> lepPhi = {fReader, "lepPhi"};
   TTreeReaderArray<float> lepM = {fReader, "lepM"};
   TTreeReaderArray<float> lepD0 = {fReader, "lepD0"};
   TTreeReaderArray<float> lepD0Sig = {fReader, "lepD0Sig"};
   TTreeReaderArray<float> lepZ0 = {fReader, "lepZ0"};
   TTreeReaderArray<float> lepZ0SinTheta = {fReader, "lepZ0SinTheta"};
   TTreeReaderArray<float> lepTopoetcone20 = {fReader, "lepTopoetcone20"};
   TTreeReaderArray<float> lepTopoetcone30 = {fReader, "lepTopoetcone30"};
   TTreeReaderArray<float> lepPtvarcone20 = {fReader, "lepPtvarcone20"};
   TTreeReaderArray<float> lepPtvarcone30 = {fReader, "lepPtvarcone30"};
   TTreeReaderArray<float> lepCorrTopoetcone20 = {fReader, "lepCorrTopoetcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone20 = {fReader, "lepCorrPtvarcone20"};
   TTreeReaderArray<float> lepCorrPtvarcone30 = {fReader, "lepCorrPtvarcone30"};
   TTreeReaderValue<vector<bool>> lepPassOR = {fReader, "lepPassOR"};
   TTreeReaderArray<int> lepType = {fReader, "lepType"};
   TTreeReaderArray<int> lepOrigin = {fReader, "lepOrigin"};
   TTreeReaderArray<int> lepEgMotherType = {fReader, "lepEgMotherType"};
   TTreeReaderArray<int> lepEgMotherOrigin = {fReader, "lepEgMotherOrigin"};
   TTreeReaderArray<int> lepEgMotherPdgId = {fReader, "lepEgMotherPdgId"};
   TTreeReaderArray<int> lepECIDS = {fReader, "lepECIDS"};
   TTreeReaderValue<vector<bool>> lepIsHF = {fReader, "lepIsHF"};
   TTreeReaderValue<vector<bool>> lepIsLF = {fReader, "lepIsLF"};
   TTreeReaderValue<vector<bool>> lepIsCO = {fReader, "lepIsCO"};
   TTreeReaderValue<vector<bool>> lepIsCF = {fReader, "lepIsCF"};
   TTreeReaderValue<vector<bool>> lepIsUK = {fReader, "lepIsUK"};
   TTreeReaderValue<vector<bool>> lepIsPR = {fReader, "lepIsPR"};
   TTreeReaderValue<vector<bool>> lepPassBL = {fReader, "lepPassBL"};
   TTreeReaderValue<vector<bool>> lepVeryLoose = {fReader, "lepVeryLoose"};
   TTreeReaderValue<vector<bool>> lepLoose = {fReader, "lepLoose"};
   TTreeReaderValue<vector<bool>> lepMedium = {fReader, "lepMedium"};
   TTreeReaderValue<vector<bool>> lepTight = {fReader, "lepTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCHighPtCaloOnly = {fReader, "lepIsoFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoFixedCutHighPtTrackOnly = {fReader, "lepIsoFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoGradient = {fReader, "lepIsoGradient"};
   TTreeReaderValue<vector<bool>> lepIsoFCLoose = {fReader, "lepIsoFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoFCTight = {fReader, "lepIsoFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoFCTightTrackOnly = {fReader, "lepIsoFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCHighPtCaloOnly = {fReader, "lepIsoCorrFCHighPtCaloOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFixedCutHighPtTrackOnly = {fReader, "lepIsoCorrFixedCutHighPtTrackOnly"};
   TTreeReaderValue<vector<bool>> lepIsoCorrGradient = {fReader, "lepIsoCorrGradient"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCLoose = {fReader, "lepIsoCorrFCLoose"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTight = {fReader, "lepIsoCorrFCTight"};
   TTreeReaderValue<vector<bool>> lepIsoCorrFCTightTrackOnly = {fReader, "lepIsoCorrFCTightTrackOnly"};
   TTreeReaderValue<vector<bool>> lepTruthMatched = {fReader, "lepTruthMatched"};
   TTreeReaderArray<int> lepTruthCharge = {fReader, "lepTruthCharge"};
   TTreeReaderArray<float> lepTruthPt = {fReader, "lepTruthPt"};
   TTreeReaderArray<float> lepTruthEta = {fReader, "lepTruthEta"};
   TTreeReaderArray<float> lepTruthPhi = {fReader, "lepTruthPhi"};
   TTreeReaderArray<float> lepTruthM = {fReader, "lepTruthM"};
   TTreeReaderValue<Int_t> nJet30 = {fReader, "nJet30"};
   TTreeReaderValue<Int_t> nJet20 = {fReader, "nJet20"};
   TTreeReaderValue<Int_t> nBJet20_MV2c10_FixedCutBEff_77 = {fReader, "nBJet20_MV2c10_FixedCutBEff_77"};
   TTreeReaderArray<float> jetPt = {fReader, "jetPt"};
   TTreeReaderArray<float> jetEta = {fReader, "jetEta"};
   TTreeReaderArray<float> jetPhi = {fReader, "jetPhi"};
   TTreeReaderArray<float> jetM = {fReader, "jetM"};
   TTreeReaderArray<float> jetJVT = {fReader, "jetJVT"};
   TTreeReaderValue<Float_t> mjj = {fReader, "mjj"};
   TTreeReaderArray<float> jetTileEnergy = {fReader, "jetTileEnergy"};
   TTreeReaderArray<float> jetMV2c10 = {fReader, "jetMV2c10"};
   TTreeReaderValue<Float_t> met_Et = {fReader, "met_Et"};
   TTreeReaderValue<Float_t> met_Sign = {fReader, "met_Sign"};
   TTreeReaderValue<Float_t> met_Phi = {fReader, "met_Phi"};
   TTreeReaderValue<Float_t> met_Et_loose = {fReader, "met_Et_loose"};
   TTreeReaderValue<Float_t> met_Et_tighter = {fReader, "met_Et_tighter"};
   TTreeReaderValue<Float_t> met_Et_tenacious = {fReader, "met_Et_tenacious"};
   TTreeReaderValue<Float_t> met_Phi_loose = {fReader, "met_Phi_loose"};
   TTreeReaderValue<Float_t> met_Phi_tighter = {fReader, "met_Phi_tighter"};
   TTreeReaderValue<Float_t> met_Phi_tenacious = {fReader, "met_Phi_tenacious"};
   TTreeReaderValue<Float_t> mll = {fReader, "mll"};
   TTreeReaderValue<Double_t> pileupWeight = {fReader, "pileupWeight"};
   TTreeReaderValue<Double_t> leptonWeight = {fReader, "leptonWeight"};
   TTreeReaderValue<Double_t> eventWeight = {fReader, "eventWeight"};
   TTreeReaderValue<Double_t> genWeight = {fReader, "genWeight"};
   TTreeReaderValue<Double_t> bTagWeight = {fReader, "bTagWeight"};
   TTreeReaderValue<Double_t> jvtWeight = {fReader, "jvtWeight"};
   // TTreeReaderValue<Double_t> genWeightUp = {fReader, "genWeightUp"};
   // TTreeReaderValue<Double_t> genWeightDown = {fReader, "genWeightDown"};
   TTreeReaderValue<Double_t> globalDiLepTrigSF = {fReader, "globalDiLepTrigSF"};
   TTreeReaderValue<Bool_t> is2Lep2Jet = {fReader, "is2Lep2Jet"};
   TTreeReaderValue<Bool_t> is2L2JInt = {fReader, "is2L2JInt"};
   TTreeReaderValue<Bool_t> is3Lep = {fReader, "is3Lep"};
   TTreeReaderValue<Bool_t> is3LInt = {fReader, "is3LInt"};
   TTreeReaderValue<Bool_t> is3Lep2Jet = {fReader, "is3Lep2Jet"};
   TTreeReaderValue<Bool_t> is3Lep3Jet = {fReader, "is3Lep3Jet"};
   TTreeReaderValue<Bool_t> is4Lep2Jet = {fReader, "is4Lep2Jet"};
   TTreeReaderValue<Bool_t> is4Lep3Jet = {fReader, "is4Lep3Jet"};
   TTreeReaderValue<Double_t> mll_RJ = {fReader, "mll_RJ"};
   TTreeReaderValue<Double_t> H2PP = {fReader, "H2PP"};
   TTreeReaderValue<Double_t> H5PP = {fReader, "H5PP"};
   TTreeReaderValue<Double_t> RPT_HT5PP = {fReader, "RPT_HT5PP"};
   TTreeReaderValue<Double_t> R_minH2P_minH3P = {fReader, "R_minH2P_minH3P"};
   TTreeReaderValue<Double_t> R_H2PP_H5PP = {fReader, "R_H2PP_H5PP"};
   TTreeReaderValue<Double_t> dphiVP = {fReader, "dphiVP"};
   TTreeReaderValue<Double_t> minDphi = {fReader, "minDphi"};
   TTreeReaderValue<Double_t> mTW = {fReader, "mTW"};
   TTreeReaderValue<Double_t> H4PP = {fReader, "H4PP"};
   TTreeReaderValue<Double_t> RPT_HT4PP = {fReader, "RPT_HT4PP"};
   TTreeReaderValue<Double_t> R_HT4PP_H4PP = {fReader, "R_HT4PP_H4PP"};
   TTreeReaderValue<Double_t> PTISR = {fReader, "PTISR"};
   TTreeReaderValue<Double_t> RISR = {fReader, "RISR"};
   TTreeReaderValue<Double_t> PTI = {fReader, "PTI"};
   TTreeReaderValue<Double_t> dphiISRI = {fReader, "dphiISRI"};
   TTreeReaderValue<Double_t> PTCM = {fReader, "PTCM"};
   TTreeReaderValue<Double_t> NjS = {fReader, "NjS"};
   TTreeReaderValue<Double_t> NjISR = {fReader, "NjISR"};
   TTreeReaderValue<Double_t> MZ = {fReader, "MZ"};
   TTreeReaderValue<Double_t> MJ = {fReader, "MJ"};
   TTreeReaderValue<Double_t> mTl3 = {fReader, "mTl3"};
   TTreeReaderValue<Double_t> lept1Pt_VR = {fReader, "lept1Pt_VR"};
   TTreeReaderValue<Double_t> lept1sign_VR = {fReader, "lept1sign_VR"};
   TTreeReaderValue<Double_t> lept2Pt_VR = {fReader, "lept2Pt_VR"};
   TTreeReaderValue<Double_t> lept2sign_VR = {fReader, "lept2sign_VR"};
   TTreeReaderValue<Double_t> mll_RJ_VR = {fReader, "mll_RJ_VR"};
   TTreeReaderValue<Double_t> H2PP_VR = {fReader, "H2PP_VR"};
   TTreeReaderValue<Double_t> H5PP_VR = {fReader, "H5PP_VR"};
   TTreeReaderValue<Double_t> RPT_HT5PP_VR = {fReader, "RPT_HT5PP_VR"};
   TTreeReaderValue<Double_t> R_minH2P_minH3P_VR = {fReader, "R_minH2P_minH3P_VR"};
   TTreeReaderValue<Double_t> R_H2PP_H5PP_VR = {fReader, "R_H2PP_H5PP_VR"};
   TTreeReaderValue<Double_t> dphiVP_VR = {fReader, "dphiVP_VR"};
   TTreeReaderValue<Double_t> PTISR_VR = {fReader, "PTISR_VR"};
   TTreeReaderValue<Double_t> RISR_VR = {fReader, "RISR_VR"};
   TTreeReaderValue<Double_t> PTI_VR = {fReader, "PTI_VR"};
   TTreeReaderValue<Double_t> dphiISRI_VR = {fReader, "dphiISRI_VR"};
   TTreeReaderValue<Double_t> PTCM_VR = {fReader, "PTCM_VR"};
   TTreeReaderValue<Double_t> NjS_VR = {fReader, "NjS_VR"};
   TTreeReaderValue<Double_t> NjISR_VR = {fReader, "NjISR_VR"};
   TTreeReaderValue<Double_t> MZ_VR = {fReader, "MZ_VR"};
   TTreeReaderValue<Double_t> MJ_VR = {fReader, "MJ_VR"};
   TTreeReaderValue<ULong64_t> PRWHash = {fReader, "PRWHash"};
   TTreeReaderValue<ULong64_t> EventNumber = {fReader, "EventNumber"};
   TTreeReaderValue<Float_t> xsec = {fReader, "xsec"};
   TTreeReaderValue<Float_t> TrueHt = {fReader, "TrueHt"};
   TTreeReaderValue<Int_t> DatasetNumber = {fReader, "DatasetNumber"};
   TTreeReaderValue<Int_t> RunNumber = {fReader, "RunNumber"};
   TTreeReaderValue<Int_t> RandomRunNumber = {fReader, "RandomRunNumber"};
   TTreeReaderValue<Int_t> FS = {fReader, "FS"};
    */

   MySelector(TTree * /*tree*/ =0) { }
   virtual ~MySelector() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();
   
   //Created by me
   bool isSignalLep(int index, TString iso_point);
   bool WantedLightJets(int nWanted, int njetslight);
   bool WantedBJets(int nWanted,int njetsB);
   bool Sign(string sign, int lepIndex1, int lepIndex2); 
   bool Flavor(string flavor, int lepIndex1, int lepIndex2);
   bool mll_cut(string largerORsmaller, float mll_cut_value_low,float mll_cut_value_high );
   bool rmZpeak(int dist_from_Z);
   bool lepPt_cut(string largerORsmaller, int lepIndex1, int lepIndex2, float lepPt_cut_value);
   bool met_Et_cut(string largerORsmaller, float met_Et_cut_value_low, float met_Et_cut_value_high);
   bool met_Sign_cut(string largerORsmaller, float met_Sign_cut_value_low, float met_Sign_cut_value_high);
   bool mT2_cut(string binned, float limit_low, float limit_high);



   ClassDef(MySelector,0);

};

#endif


#ifdef MySelector_cxx
void MySelector::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the reader is initialized.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   fReader.SetTree(tree);
}

Bool_t MySelector::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}


#endif // #ifdef MySelector_cxx

