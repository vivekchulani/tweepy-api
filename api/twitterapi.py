# Python script to fetch real time twitter data
from listener import *

import sys
import json
import tweepy # twitter api wrapper

# Tweepy Documentation used for Reference
# https://tweepy.readthedocs.io/en/v3.5.0/index.html

# Load text file with credentials
credentials = {}
try:
    with open("credentials.txt", "r") as cred:
        data = cred.readlines()
    for line in data:
        (key, value) = line.rstrip("\n").split("=")
        credentials[key] = value
except IOError:
    print("Error reading file")
except FileNotFoundError:
    print("File not found")

# Create OAuth instance
(apiKey, apiSecret, accessToken, accessSecret) = (credentials["api_key"], credentials["api_secret"], credentials["access_token"], credentials["acces_secret"])
auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth, retry_delay=15, retry_errors=420)

# Twitter Documentation for Filtering real time tweets
# https://developer.twitter.com/en/docs/tweets/filter-realtime/overview/statuses-filter
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object

# Create stream instance
streamListener = StreamListener()
sl = tweepy.Stream(auth = api.auth, listener = streamListener, tweet_mode='extended')

# Start stream based on input rules
# Track all tweets for companies listed in S&P500 since track is limited to 400 keywords
sl.filter(track = ['$ABT', '$ABBV', '$ACN', '$ACE', '$ADBE', '$ADT', '$AAP', '$AES',
'$AET', '$AFL', '$AMG', '$A', '$GAS', '$APD', '$ARG', '$AKAM', '$AA',
'$AGN', '$ALXN', '$ALLE', '$ADS', '$ALL', '$ALTR', '$MO','$AMZN', '$AEE',
'$AAL','$AEP', '$AXP', '$AIG', '$AMT', '$AMP', '$ABC', '$AME', '$AMGN',
'$APH','$APC', '$ADI', '$AON', '$APA', '$AIV', '$AMAT', '$ADM', '$AIZ', '$T',
'$ADSK', '$ADP', '$AN', '$AZO','$AVGO', '$AVB', '$AVY', '$BHI', '$BLL',
'$BAC', '$BK', '$BCR', '$BXLT', '$BAX', '$BBT', '$BDX', '$BBBY', '$BRK-B',
'$BBY', '$BLX', '$HRB', '$BA', '$BWA', '$BXP', '$BSK', '$BMY', '$BRCM',
'$BF-B', '$CHRW','$CA', '$CVC', '$COG', '$CAM', '$CPB', '$COF', '$CAH',
'$HSIC', '$KMX', '$CCL', '$CAT', '$CBG', '$CBS', '$CELG', '$CNP', '$CTL',
'$CERN', '$CF', '$SCHW', '$CHK', '$CVX', '$CMG', '$CB', '$CI', '$XEC',
'$CINF', '$CTAS', '$CSCO', '$C', '$CTXS', '$CLX', '$CME', '$CMS', '$COH',
'$KO', '$CCE', '$CTSH', '$CL', '$CMCSA', '$CMA', '$CSC', '$CAG', '$COP',
'$CNX', '$ED', '$STZ', '$GLW', '$COST', '$CCI', '$CSX',
'$CMI', '$CVS', '$DHI', '$DHR', '$DRI', '$DVA', '$DE', '$DLPH', '$DAL',
'$XRAY', '$DVN', '$DO', '$DTV', '$DFS', '$DISCA', '$DISCK', '$DG', '$DLTR',
'$D', '$DOV', '$DOW', '$DPS', '$DTE', '$DD', '$DUK',
'$DNB', '$ETFC', '$EMN', '$ETN', '$EBAY', '$ECL', '$EIX', '$EW', '$EA',
'$EMC', '$EMR', '$ENDP', '$ESV', '$ETR', '$EOG', '$EQT', '$EFX', '$EQIX',
'$EQR', '$ESS', '$EL', '$ES', '$EXC', '$EXPE', '$EXPD',
'$ESRX', '$XOM', '$FFIV', '$FB', '$FAST', '$FDX', '$FIS', '$FITB',
'$FSLR', '$FE', '$FSIV', '$FLIR', '$FLS', '$FLR', '$FMC', '$FTI', '$F',
'$FOSL', '$BEN', '$FCX', '$FTR', '$GME', '$GPS', '$GRMN', '$GD',
'$GE', '$GGP', '$GIS', '$GM', '$GPC', '$GNW', '$GILD', '$GS', '$GT',
'$GOOGL', '$GOOG', '$GWW', '$HAL', '$HBI', '$HOG', '$HAR', '$HRS', '$HIG',
'$HAS', '$HCA', '$HCP', '$HCN', '$HP', '$HES', '$HPQ',
'$HD', '$HON', '$HRL', '$HSP', '$HST', '$HCBK', '$HUM', '$HBAN', '$ITW',
'$IR', '$INTC', '$ICE', '$IBM', '$IP', '$IPG', '$IFF', '$INTU', '$ISRG',
'$IVZ', '$IRM', '$JEC', '$JBHT', '$JNJ', '$JCI', '$JOY',
'$JPM', '$JNPR', '$KSU', '$K', '$KEY', '$GMCR', '$KMB', '$KIM', '$KMI',
'$KLAC', '$KSS', '$KRFT', '$KR', '$LB', '$LLL', '$LH', '$LRCX', '$LM',
'$LEG', '$LEN', '$LVLT', '$LUK', '$LLY', '$LNC', '$LLTC',
'$LMT', '$L', '$LOW', '$LYB', '$MTB', '$MAC', '$M', '$MNK', '$MRO', '$MPC',
'$MAR', '$MMC', '$MLM', '$MAS', '$MA', '$MAT', '$MKC', '$MCD', '$MHFI',
'$MCK', '$MJN', '$MMV', '$MDT', '$MRK', '$MET',
'$KORS', '$MCHP', '$MU', '$MSFT', '$MHK', '$TAP', '$MDLZ', '$MON', '$MNST',
'$MCO', '$MS', '$MOS', '$MSI', '$MUR', '$MYL', '$NDAQ', '$NOV', '$NAVI',
'$NTAP', '$NFLX', '$NWL', '$NFX', '$NEM', '$NWSA', '$NEE',
'$NLSN', '$NKE', '$NI', '$NE', '$NBL', '$JWN', '$NSC', '$NTRS', '$NOC',
'$NRG', '$NUE', '$NVDA', '$ORLY', '$OXY', '$OMC', '$OKE', '$ORCL', '$OI',
'$PCAR', '$PLL', '$PH', '$PDCO', '$PAYX', '$PNR', '$PBCT',
'$POM', '$PBI', '$PCL', '$PNC', '$RL', '$PPG', '$PPL', '$PX', '$PCP',
'$PCLN', '$PFG', '$PG', '$PGR', '$PLD', '$PRU', '$PEG', '$PSA', '$PHM',
'$PVH', '$QRVO', '$PWR', '$QCOM', '$DGX', '$RRC', '$RTN',
'$O', '$RHT', '$REGN', '$RF', '$RSG', '$RAI', '$RHI', '$ROK', '$COL',
'$ROP', '$ROST', '$RLC', '$R', '$CRM', '$SNDK', '$SCG', '$SLB', '$SNI',
'$STX', '$SEE', '$SRE', '$SHW', '$SIAL', '$SPG', '$SPY'], languages = ['en'])
