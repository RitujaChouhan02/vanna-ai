from vanna_setup import vn

# ✅ Allow the LLM to inspect schema/data
vn.allow_llm_to_see_data = True

schema = """
CREATE TABLE tblusers (
    user_id Float64,
    first_name String,
    last_name String,
    email_id Nullable(String),
    mobile_code Nullable(String),
    mobile_no Nullable(String),
    dob String,
    type Float64,
    status Float64,
    photo Nullable(String),
    pan_name Nullable(String),
    nominee_name Nullable(String),
    nominee_relation String,
    esign String,
    occupation Nullable(Float64),
    din String,
    kyc_aadhaar_status Float64,
    kyc_pan_status Float64,
    kyc_bank_status Float64,
    kyc_esign_status Float64,
    kyc_skip Float64,
    kyc_done Float64,
    residential_status String,
    nationality String,
    user_type Float64,
    reporting Nullable(Float64),
    created_at DateTime('Asia/Kolkata'),
    last_update_at DateTime('Asia/Kolkata'),
    zoho_id String,
    lead_owner Nullable(Float64),
    referral_code Nullable(String),
    referred_by Nullable(Float64),
    partner_type Nullable(Float64),
    deleted_at Nullable(DateTime('Asia/Kolkata')),
    nominee_dob Nullable(DateTime),
    nominee_address Nullable(String),
    demat_no Nullable(String),
    tin String,
    nominee_email Nullable(String),
    politically_exposed_person String,
    country_of_birth String,
    place_of_birth String,
    enhanced_kyc_email_sent UInt8
);

CREATE TABLE tblorders (
    order_id String,
    order_date DateTime('Asia/Kolkata'),
    user_id Float64,
    asset_id Float64,
    spv_id Float64,
    amount Float64,
    wallet_amount Float64,
    partner_type Float64,
    payment_gateway_id Nullable(Float64),
    payment_method Nullable(Float64),
    pg_transaction_id String,
    document_status Float64,
    transaction_id String,
    transaction_time Nullable(DateTime),
    transaction_msg String,
    comments String,
    payment_link String,
    status Float64,
    sub_status Float64,
    created_at DateTime('Asia/Kolkata'),
    last_update_at Nullable(DateTime('Asia/Kolkata')),
    source String,
    bond_purchase_price Nullable(Float64),
    units Nullable(Float64),
    unit_price Nullable(Float64),
    is_rfq UInt8,
    payment_session_id String,
    amo_link String,
    is_amo UInt8,
    amo_link_status String,
    security_id Nullable(Float64),
    order_type String,
    units_sold Float64,
    lock_in_expiry Nullable(DateTime)
);
"""

# Add schema
vn.add_ddl(schema)
print("✅ Schema added to Vanna!")

