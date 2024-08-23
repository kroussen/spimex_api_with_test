async def test_get_last_trading_dates_api(client, mock_redis_client, clean_database, add_data):
    await clean_database()
    await add_data()

    response = await client.get('/api/last_trading_dates', params={"count_last_days": "3"})

    assert response.status_code == 200
    assert response.json() == ['2023-05-10', '2023-04-20', '2023-03-01']

    mock_redis_client.get.assert_called_once_with('last_trading_dates:3')


async def test_get_dynamics_api(client, mock_redis_client, clean_database, add_data):
    await clean_database()
    await add_data()

    response = await client.get('/api/dynamics', params={"start_date": "2023-01-13", "end_date": "2023-01-14"})

    assert response.status_code == 200
    assert response.json() == [{
        'count': 1,
        'date': '2023-01-13',
        'delivery_basis_id': 'ANK',
        'delivery_basis_name': 'Ангарск-группа станций',
        'delivery_type_id': 'F',
        'exchange_product_id': 'A100ANK060F',
        'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
        'id': 1,
        'oil_id': 'A100',
        'total': 3292320,
        'volume': 60
    }]

    mock_redis_client.get.assert_called_once_with('dynamics:2023-01-13:2023-01-14:None:None:None')


async def test_get_trading_results_api(client, mock_redis_client, clean_database, add_data):
    await clean_database()
    await add_data()

    response = await client.get('/api/trading_results', params={"oil_id": "A100"})

    assert response.status_code == 200
    assert response.json() == [{
        'count': 1,
        'date': '2023-01-13',
        'delivery_basis_id': 'ANK',
        'delivery_basis_name': 'Ангарск-группа станций',
        'delivery_type_id': 'F',
        'exchange_product_id': 'A100ANK060F',
        'exchange_product_name': 'Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)',
        'id': 1,
        'oil_id': 'A100',
        'total': 3292320,
        'volume': 60
    }]

    mock_redis_client.get.assert_called_once_with('trading_results:A100:None:None')
