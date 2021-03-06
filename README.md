# json_validator

Example of output:
```
event: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json
error path: required
'labels' is a required property

Failed validating 'required' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'id': {'type': ['null', 'integer']},
                    'labels': {'items': {'properties': {'category': {'type': ['null',
                                                                              'string']},
                                                        'color': {'type': ['null',
                                                                           'object']},
                                                        'is_custom_tag': {'type': 'boolean'},
                                                        'name_en': {'type': 'string'},
                                                        'name_ru': {'type': 'string'},
                                                        'property_arousal': {'type': ['string',
                                                                                      'null']},
                                                        'property_pleasure': {'type': ['string',
                                                                                       'null']},
                                                        'property_stability': {'type': ['string',
                                                                                        'null']},
                                                        'property_vitality': {'type': ['string',
                                                                                       'null']},
                                                        'property_where': {'type': ['string',
                                                                                    'null']},
                                                        'slug': {'type': 'string'},
                                                        'type': {'type': 'integer'},
                                                        'type_stress': {'type': 'integer'}},
                                         'required': ['category',
                                                      'color',
                                                      'is_custom_tag',
                                                      'name_en',
                                                      'name_ru',
                                                      'property_arousal',
                                                      'property_pleasure',
                                                      'property_stability',
                                                      'property_vitality',
                                                      'property_where',
                                                      'slug',
                                                      'type',
                                                      'type_stress'],
                                         'type': 'object'},
                               'type': 'array'},
                    'rr_id': {'type': ['null', 'integer']},
                    'timestamp': {'type': 'string'},
                    'unique_id': {'type': 'string'},
                    'user': {'properties': {'id': {'type': 'integer'}},
                             'required': ['id'],
                             'type': 'object'},
                    'user_id': {'type': 'integer'}},
     'required': ['id',
                  'labels',
                  'rr_id',
                  'timestamp',
                  'unique_id',
                  'user',
                  'user_id'],
     'type': 'object'}

On instance:
    {'created_at': '2020-09-09T11:07:45.080214Z',
     'data': {'id': None,
              'labels': [{'category': 'health-body',
                          'color': {'color': '#e83e35', 'label': 'stress'},
                          'is_custom_tag': False,
                          'name_en': 'cold/flu',
                          'name_ru': 'простуда/грипп',
                          'property_arousal': None,
                          'property_pleasure': None,
                          'property_stability': None,
                          'property_vitality': None,
                          'property_where': None,
                          'slug': 'flu',
                          'type': 2,
                          'type_stress': 2}],
              'rr_id': None,
              'timestamp': '2020-09-09T14:07:44'},
     'environment_id': 2,
     'event': 'label_selected',
     'id': 'as'}


```
