class MarketTreasuryYield:

    baseUrl = 'https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=1260500ff9e23c45cdf81a960f44bf68&file_type=json&observation_start='
    headers = None
    name = 'market_treasury_yield'
    stageTableName = 'stage_market_treasury_yield'
    tableAttributes = ['date', 'value', 'loadId']
    procedureName = 'load_core_market_treasury_yield'
    dynamicValues = '%s, %s, %s'