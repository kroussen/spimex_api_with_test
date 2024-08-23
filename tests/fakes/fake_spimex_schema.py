from source.schemas.spimex import SpimexDataSchema

FAKE_SPIMEX_DATA: list[SpimexDataSchema] = [
    SpimexDataSchema(
        id=1,
        exchange_product_id="A100ANK060F",
        exchange_product_name="Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)",
        oil_id="A100",
        delivery_basis_id="ANK",
        delivery_basis_name="Ангарск-группа станций",
        delivery_type_id="F",
        volume=60,
        total=3292320,
        count=1,
        date="2023-01-13"
    ),
    SpimexDataSchema(
        id=2,
        exchange_product_id="A95KIR055G",
        exchange_product_name="Бензин (АИ-95-К5), Киришский НПЗ (ст. отправления)",
        oil_id="A95",
        delivery_basis_id="KIR",
        delivery_basis_name="Киришский НПЗ",
        delivery_type_id="G",
        volume=55,
        total=4291015,
        count=1,
        date="2023-02-17"
    ),
    SpimexDataSchema(
        id=3,
        exchange_product_id="A92UFA070F",
        exchange_product_name="Бензин (АИ-92-К5), Уфа-Группы станций (ст. отправления)",
        oil_id="A92",
        delivery_basis_id="UFA",
        delivery_basis_name="Уфа-Группы станций",
        delivery_type_id="F",
        volume=70,
        total=5019345,
        count=1,
        date="2023-03-01"
    ),
    SpimexDataSchema(
        id=4,
        exchange_product_id="A95TUP075H",
        exchange_product_name="Бензин (АИ-95-К5), Туапсе НПЗ (ст. отправления)",
        oil_id="A95",
        delivery_basis_id="TUP",
        delivery_basis_name="Туапсе НПЗ",
        delivery_type_id="H",
        volume=75,
        total=6021489,
        count=1,
        date="2023-04-20"
    ),
    SpimexDataSchema(
        id=5,
        exchange_product_id="A92NKM065G",
        exchange_product_name="Бензин (АИ-92-К5), Нижнекамск НПЗ (ст. отправления)",
        oil_id="A92",
        delivery_basis_id="NKM",
        delivery_basis_name="Нижнекамск НПЗ",
        delivery_type_id="G",
        volume=65,
        total=7183012,
        count=1,
        date="2023-05-10"
    )
]
