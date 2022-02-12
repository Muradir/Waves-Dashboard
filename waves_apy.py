class WavesApy:

    url = 'https://dev.pywaves.org/neutrino/json'
    headers = None
    tableName = 'stage_waves_apy'
    tableAttributes = ['30d', '60d', '7d', 'last', '3d', 'dateOfToday', 'loadId']
    dynamicValues = '%s, %s, %s, %s, %s, %s, %s'