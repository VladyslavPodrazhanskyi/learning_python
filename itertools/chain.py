import itertools

arguments = {
    "enriched_sap_pn4_finance_db_name": 'a',
    "enriched_fra_nc_db_name": 'b',
    "enriched_finance_nc_db_name": 'c',
    "enriched_sap_pn4_db_name": 'd',
    "enriched_iafa_db_name": 'e',
    "enriched_iafa_bucket_name": 'f'
}

manual_arguments = list(
        itertools.chain(*(
            ['--{arg_name}'.format(arg_name=arg_name), arg_value]
            for arg_name, arg_value in arguments.items()
        ))
    )

print(manual_arguments)
