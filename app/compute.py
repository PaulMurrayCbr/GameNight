
def compute_character(ch):
    
    unsourced_effects = [
        {
            'amt': 2,
            'to': 'AC',
            'type': 'morale'
        }
    ]
    
    return {
        'current' : {
            'unsourced': unsourced_effects
        },
        'computed': {
            'AC' : {
                'breakdown' : [
                    { 'type': 'morale', 'amt' : 2}
                ],
                'total' : 2
            }
        }
    }