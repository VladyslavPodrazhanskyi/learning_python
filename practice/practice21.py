columns = '''
order_apr
dri_credit_app_id
deal_ref_id
monthly_payment
dri_term
total_amount_financed
vehicle_sale_price
tenant_id
order_number
user_id
creation_date
last_update_date
vin
vehicle_make
vehicle_model
vehicle_trim
vehicle_mileage
vehicle_year
aftermarket_products
retailer_id
request_vin
request_loantovalueratio
request_vehicleyear
request_mileage
request_make
request_model
request_trim
request_retailvalue
request_invoiceamount
request_estamountfinanced
individual_lender_probs
response_buyrate
response_dealerreserve
response_sellrate
request_term
request_score
request_salaryannual
request_cashdownamount
request_state
request_dealpostcovid
dri_user
dri_coreid
dri_tenantid
rate_model
lender_qualification_model
qualification_model_threshold
comments
lambda_timestamp
request_ageofcredit
request_autotrades
request_satisfactoryaccounts
request_derogatoryaccounts
request_numtradeswithdelinquency
request_revolvingcreditbalancepercent
request_autoinquiries
request_numopenautoaccounts
request_agenewestautoaccount
request_openautoaccounts
response_info_buyrate
response_info_dealerreserve
response_info_sellrate
response_info_suggestedcashdownamount
response_info_suggestedterm
response_info_suggestedchangeincashdownamount
response_info_reason
request_ficoscorev8
request_date_feature
request_ismqdeclined
request_mqexceptions
request_sourcepartnerdealerid
request_sourcepartnerid
used_model_featuresv2
response_error_code
response_error_message
response_error_property
individual_lender_preds
lender_model
used_model_features
request_pricingprofile
request_tradeinamount
response_exception
vin_num
auto_trim
mileage
sbmt_date
processed_postalcode
origl_submit_timestamp_submission_key
app_modified_userid
app_user_id
branding_id
chromestyleid
co_app_cc_id
countryid
cr_analyst_user_id
credit_app_id
credit_app_id_short
deal_id
deal_jacket_id
dealer_id
dealer_updtd_by_user_id
doc_analyst_user_id
lender_dealer_id
lendr_app_id
primary_app_cc_id
stateid
vehicle_id
buy_rate
contract_rate
cust_rate
rqstd_apr_rt
app_drpts_decision
appl_decision
contract_decision
deal_stus_cd
feature_stus_cd
rollout_stus_in
agmnt_rqd_by_dt
book_dt
con_drpts_date
created_ts
customer_created_ts
customer_updtd_ts
date_submitted_creditapp
dealer_created_ts
dealer_updtd_ts
dealerstatusdatetimedtc
decision_date
doc_received_ts
received_timestamp_submission
enrl_dt
first_decision_rcvd_date
fnl_dlvry_ts
fund_date
good_until_date
invce_ts
invnty_ts
last_survey_ts
request_date
rollout_stus_ts
sbmt_ts
shpd_ts
sold_ts
updtd_ts
addressline1
city
enrl_phase_cd
enrolledstatusflag
dealer_created_by_user_cd
dealer_updtd_by_user_cd
dealercode
dealerlegalname
dealername
dealerremark
dealerstatuscodedtc
dlr_cust_service_phone
dlrshp_tm_zone_cd
dlrshp_typ_cd
dlrshp_use_cd
postalcode
primarydealergroupcode
primarydealergroupname
state
telephone
accident_health_insce_am
acquistion_fee_am
amt_financed
aprv_loan_amt
back_end_fee_am
balloon_paymt_am
cap_cst_am
cash_down_am
cash_sell_prc_am
con_acquisition_fee_am
credit_life_insce_am
cust_money_fctr_am
disbursed_am
dlr_bonus_am
dlr_pctpn_am
down_payment
est_amt_financed
est_payment
estmd_balloon_am
first_pay_deduct
front_end_fee_am
gap
gap_dlr_amt
invoice_am
lender_money_fctror_am
monthly_pmt
msrp_am
official_fees
other_finance_fees
payment_call_amt
paymt_am
rebate_am
req_amount
residual_val_am
scrty_deposit_am
sls_tax_am
subvention_amt
title_and_lic_am
trade_in_val_am
trade_monthly_payment
unpaid_balance_am
warranty_am
wholesale_am
auto_make
auto_model
auto_year
buy_veh_in
condition
certified_used
classification
engn_typ_nm
fuel_typ_nm
input_make_nm
input_model_nm
input_style_nm
input_trim_nm
input_yr_nb
manufacturer
new_used_cd
retail_value
tradein_auto_make
tradein_auto_model
tradein_auto_trim
tradein_auto_year
tradein_mileage
trim_nm
tradein_vin_num
veh_other
app_contract_ind
app_created
app_source
app_typ_cd
bonus_reserve_ind
book_translated
bookout
busn_typ_cd
buying_spectrum
deal_typ_cd
deal_updt_elig_in
dspn_cd
econ_eligible_in
econtract_ind
empl_ct
eq_fico_score
ex_fico_score
fico_score_band_cd
grace_prd_cd
high_score
is_busn_in
is_lender_booked
dt_ltv
loan_type
lot_loc_nm
low_score
optout_ind
pass_thru_app_in
pass_thru_xcld_in
paymt_call_in_deal
pkg_cd
pre_app_in
red_flag_in
req_product
rooftop_in
source
sourcesystem
spot_ind
submitted
term
tier_lvl_nm
trade_financed
tu_fico_score
months_employed
mortgage_paymt_or_rent_am
postal_cd
salary_annual
activ_inactiv_ind
feature_cd
full_style_cd
stock_num
hashed_lender_id
employment_status_code
ext_ref_id
ext_src_cd
upload_date
vehicle_ids
trim_api
make_api
model_api
model_year_api
match_rate
avg_adjusted_value
loan_to_val_rt
lender_predicted_prob
lender_predicted_rate
lender_routing_vin
lender_routing_lenders
lender_routing_errorcodes
lender_routing_maxlendernumber
lender_routing_probabilitythreshold
lender_routing_eventtimestamp
lender_routing_ismqdeclined
lender_routing_pricingprofile
lender_routing_userid
lender_routing_ordernumber
lender_routing_lenderprobs
lender_routing_currentjobyears
lender_routing_annualincome
lender_routing_bankruptcies
lender_routing_satisfactoryaccounts
lender_routing_maxlendernumbers
lender_routing_ficoscore
lender_selection_vin
lender_selection_userid
lender_selection_lenderdecisions
lender_selection_lenderid
lender_selection_defaultlender
lender_selection_profitsv2
lender_selection_sortedlenders
lender_selection_filteredoutdecisions
lender_selection_pricingprofile
lender_selection_eventtimestamp
lender_selection_ismqdeclined
lender_selection_errorcodes
lender_selection_cashdown
lender_selection_term
lender_selection_negativevariancecutoff
year
month
day
'''

list_col = ', '.join(columns.split('\n')[1:-1])

print(list_col)

