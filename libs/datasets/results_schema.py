from libs.datasets import CommonFields

# TODO - maybe make this full name
STATE = CommonFields.STATE_FULL_NAME
COUNTRY = "Country/Region"
LAST_UPDATED = "Last Update"
LATITUDE = "Latitude"
LONGITUDE = "Longitude"
FIPS = CommonFields.FIPS
STATE_INTERVENTION = 'State Intervention'
SIXTEEN_DAY_HOSPITALIZATION = '16d-HSPTLZD'
THIRTY_TWO_DAY_HOSPITALIZATION = '32d-HSPTLZD'
SIXTEEN_DAY_LACK_BED = '16d-LACKBEDS'
THIRTY_TWO_DAY_LACK_BED = '32d-LACKBEDS'
MEAN_HOSPITALIZATIONS = 'MEAN-HOSP'
MEAN_DEATHS = 'MEAN-DEATHS'
PEAK_HOSPITALIZATIONS = 'PEAK-HOSP'
PEAK_DEATHS = 'PEAK-DEATHS'
CURRENT_DEATHS = "Current Deaths"
CURRENT_CONFIRMED = "Current Confirmed"
COMBINED_KEY = "Combined Key"
COUNTY = "County"
HOSPITAL_SHORTFALL_DATE = "Hospital Shortfall Date"
PEAK_HOSPITALIZATION_SHORTFALL = "Peak Hospitlizations Shortfall"
PEAK_BED_CAPACITY = "Peak Bed Capacity"
POPULATION = "Population"
RT = "Rt"
RT_CI90 = "Rt_ci90"

RESULT_DATA_COLUMNS_SHARED = [
    STATE,
    COUNTRY,
    LAST_UPDATED,
    LATITUDE,
    LONGITUDE,
    FIPS,
    STATE_INTERVENTION,
    SIXTEEN_DAY_HOSPITALIZATION,
    THIRTY_TWO_DAY_HOSPITALIZATION,
    SIXTEEN_DAY_LACK_BED,
    THIRTY_TWO_DAY_LACK_BED,
    MEAN_HOSPITALIZATIONS,
    MEAN_DEATHS,
    PEAK_HOSPITALIZATIONS,
    PEAK_DEATHS,
    CURRENT_DEATHS,
    CURRENT_CONFIRMED,
    COMBINED_KEY,
    COUNTY,
    HOSPITAL_SHORTFALL_DATE,
    PEAK_HOSPITALIZATION_SHORTFALL,
    PEAK_BED_CAPACITY,
    POPULATION,
    RT,
    RT_CI90
]

NON_INTEGER_FIELDS = [
    STATE_INTERVENTION,
    PEAK_HOSPITALIZATIONS,
    PEAK_DEATHS,
    HOSPITAL_SHORTFALL_DATE,
    PEAK_HOSPITALIZATION_SHORTFALL,
    STATE,
    COUNTRY,
    LAST_UPDATED,
    COMBINED_KEY,
    COUNTY,
    FIPS,
    RT,
    RT_CI90
]

SHAPEFILE_FIELDS = [
    STATE_INTERVENTION,
    SIXTEEN_DAY_HOSPITALIZATION,
    THIRTY_TWO_DAY_HOSPITALIZATION,
    SIXTEEN_DAY_LACK_BED,
    THIRTY_TWO_DAY_LACK_BED,
    MEAN_HOSPITALIZATIONS,
    MEAN_DEATHS,
    PEAK_HOSPITALIZATIONS,
    PEAK_DEATHS,
    CURRENT_DEATHS,
    CURRENT_CONFIRMED,
    HOSPITAL_SHORTFALL_DATE,
    PEAK_HOSPITALIZATION_SHORTFALL,
    PEAK_BED_CAPACITY,
]

CUMULATIVE_POSITIVE_TESTS = 'Cumulative Tested Positive'
CUMULATIVE_NEGATIVE_TESTS = 'Cumulative Tested Negative'

RESULT_DATA_COLUMNS_STATES = RESULT_DATA_COLUMNS_SHARED + [CUMULATIVE_POSITIVE_TESTS, CUMULATIVE_NEGATIVE_TESTS]
RESULT_DATA_COLUMNS_COUNTIES = RESULT_DATA_COLUMNS_SHARED + []

EXPECTED_MISSING_STATES = set([
    'Northern Mariana Islands', 'American Samoa', 'Virgin Islands', 'Puerto Rico', 'Guam'
])

EXPECTED_MISSING_STATES_FROM_COUNTES = set([
    'District of Columbia'
])
