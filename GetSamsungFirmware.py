#!/usr/bin/env python3

import requests
from xml.etree import cElementTree as ET

Endpoint = "http://fota-cloud-dn.ospserver.net/"
MODEL = "SM-N950F"
BETA = False

CSC_List = ["AFG", "TMC", "ALG", "ALR", "ATO", "AOM", "DRE", "MAX", "MOB",
"ONE", "TRG", "TTR", "AFV", "ARU", "XSA", "OPP", "OPS", "VAU", "TEL",
"HUT", "ANC", "ARO", "CTI", "UFN", "PSN", "ARB", "SEB", "MTB", "VEL",
"BSE", "BAE", "PRO", "XEB", "BNG", "TML", "ETR", "ERO", "BHO", "BHT",
"TEB", "ZTO", "BTA", "BTM", "TMR", "ZTA", "ZVV", "ZTM", "BGL", "CMF",
"GBL", "MTE", "MTL", "OMX", "PLX", "VVT", "CAM", "RCG", "BMC", "RWC",
"TLS", "KDO", "CHO", "CHB", "CHE", "CHL", "CHT", "CHN", "CMC", "CUH",
"INT", "M00", "TEC", "TIY", "COO", "CGU", "COB", "COL", "COM", "ICE",
"CRO", "TRA", "TWO", "VIP", "DHR", "CYV", "CYO", "ETL", "KBN", "O2C",
"OSK", "TMZ", "VDC", "XCS", "XEZ", "CAU", "DTL", "CDR", "TDR", "DOR",
"CST", "DCN", "DOR", "EBE", "ECO", "BBR", "EGY", "DGC", "TBS", "ELS",
"SAU", "XEF", "AUC", "BOG", "COR", "DIX", "FTM", "NRJ", "OFR", "ORC",
"ORF", "OXA", "SFR", "UNI", "VGF", "VFJ", "DBT", "DTM", "DUT", "EPL",
"MAN", "MBC", "OXA", "VD2", "VIA", "XEG", "SPN", "ACR", "EUR", "AOC",
"COS", "CYO", "GER", "OXX", "TGR", "VGR", "ILO", "PCS", "TGU", "PGU",
"CGU", "TGY", "XEH", "PAN", "VDH", "WST", "TMO", "TMH", "INU", "IND",
"INA", "INS", "IMS", "REL", "AXI", "SAR", "XSE", "XID", "THR", "MID",
"3IE", "VDI", "TSI", "MET", "ILO", "CEL", "PCL", "PTR", "ITV", "FWB",
"GOM", "HUI", "OMN", "OXA", "TIM", "VOM", "WIN", "XET", "IRS", "SIE",
"JBS", "JCN", "JCW", "JDI", "CWW", "DCM", "SBM", "VFK", "LEV", "EST",
"KCL", "KMB", "KZK", "OXE", "SKZ", "KEN", "KEL", "AFR", "SKT", "LUC",
"SKC", "KTC", "SEB", "MMC", "TLT", "LUX", "VTN", "TMC", "MBM", "VIM",
"CCM", "FME", "FMG", "MXS", "OLB", "XME", "SEM", "TCE", "TMM", "UNE",
"IUS", "MPC", "FWD", "MAT", "MED", "MWD", "SNI", "WAN", "TMT", "NPL",
"PHN", "BEN", "KPN", "MMO", "ONL", "QIC", "TFT", "TNL", "VDF", "VDP",
"XEN", "VNZ", "NZC", "TNZ", "ECT", "GCR", "MML", "NEE", "TEN", "PAK",
"WDC", "TPA", "BPC", "PCW", "PBS", "CPA", "PEB", "PET", "SAM", "PNT",
"PVT", "FAM", "GLB", "OLB", "SMA", "XTC", "XTE", "ERA", "IDE", "PLS",
"PRT", "XEO", "OXA", "OXX", "DPL", "TPL", "OPT", "OXX", "TCL", "TMN",
"TPH", "XEP", "CEN", "PCI", "TPR", "PCT", "ROM", "CNX", "COA", "HAT",
"ORO", "OXX", "AZC", "BLN", "EMT", "ERS", "GEO", "MTV", "OXE", "SER",
"SNT", "KSA", "JED", "ACR", "WTL", "STC", "XFU", "DKR", "MSR", "OXX",
"PMN", "SMO", "TOP", "TSR", "MM1", "XSP", "SIN", "STH", "BGD", "XSO",
"MOT", "SIM", "SIO", "ORX", "GTL", "IRD", "ORS", "OXX", "TMS", "XFA",
"XFE", "OXX", "XFC", "XFM", "XFV", "SEE", "SWA", "PHE", "FOP", "AMN",
"ATL", "EUS", "XEC", "YOG", "SLK", "BAU", "BCN", "BME", "BSG", "BTH",
"COV", "HTS", "SEN", "TET", "TLA", "TNO", "VDS", "XEE", "AUT", "MOZ",
"ORG", "OXX", "SUN", "SWC", "BRI", "CWT", "TCC", "TCI", "TWM", "CAT",
"OLB", "THE", "THL", "THO", "THS", "LAO", "MYM", "SOL", "EON", "TTT",
"TUN", "ABS", "RNG", "TUR", "BAS", "KVK", "TLP", "TRC", "KVR", "SEK",
"UMC", "ARB", "ITO", "MID", "OXE", "XSG", "BTU", "EVR", "BTC", "CPW",
"H3G", "O2I", "O2U", "ORA", "OXA", "TMU", "TSC", "VIR", "VOD", "XEU",
"ACG", "ATT", "BST", "CCT", "GCF", "LRA", "SPR", "TFN", "TMB", "USC",
"VMU", "VZW", "XAA", "XAS", "CAC", "UZB", "VMT", "DGT", "MVL", "DNA",
"FPT", "OLB", "PHU", "SPT", "TLC", "VTC", "VTL", "XEV", "XXV", "MOK"]

Current_Latest_PDA = ""
Current_Latest_PDA_CSC = ""

for CSC in CSC_List:

    print("Checking for CSC: " + CSC)

    # http://fota-cloud-dn.ospserver.net/firmware/[CSC]/[MODEL]/version.xml
    XMLReply = requests.get(url = Endpoint + "firmware/" + CSC + "/" + MODEL + ("/version.test.xml" if BETA else "/version.xml") ).text.strip()

    if ("AccessDenied" in XMLReply):
        print("ERROR: AccessDenied, invalid CSC/Model? Skipping...")
        continue

    XMLRoot = ET.fromstring(XMLReply)

    Lastest_PDA_MDM_CSC = XMLRoot.findall('.//latest')[0].text


    if (Lastest_PDA_MDM_CSC == None):
        print("ERROR: No Firmware, skipping...")
        continue

    Latest_PDA = Lastest_PDA_MDM_CSC.split('/')[0]

    if (Latest_PDA[-5:] > Current_Latest_PDA[-5:]):
        Current_Latest_PDA = Latest_PDA
        Current_Latest_PDA_CSC = CSC

    print(Latest_PDA)

print("Latest Firmware: " + Current_Latest_PDA)
print("Latest Firmware CSC: " + Current_Latest_PDA_CSC)