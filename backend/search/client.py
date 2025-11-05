from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.search_single_index(index_name)
    return index

def perform_search(query, **kwargs):
    index = get_index()
    # print(index.hits)
    results = index
    return results



['__abstractmethods__', '__annotations__', '__class__', '__class_getitem__', '__class_vars__', '__copy__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', 
    '__doc__', '__eq__', '__fields__', '__fields_set__', '__firstlineno__', '__format__', '__ge__', '__get_pydantic_core_schema__', 
    '__get_pydantic_json_schema__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__pretty__', '__private_attributes__', '__pydantic_complete__', '__pydantic_computed_fields__', 
    '__pydantic_core_schema__', '__pydantic_custom_init__', '__pydantic_decorators__', '__pydantic_extra__', '__pydantic_fields__', '__pydantic_fields_set__', 
    '__pydantic_generic_metadata__', '__pydantic_init_subclass__', '__pydantic_on_complete__', '__pydantic_parent_namespace__', '__pydantic_post_init__', 
    '__pydantic_private__', '__pydantic_root_model__', '__pydantic_serializer__', '__pydantic_setattr_handlers__', '__pydantic_validator__', '__reduce__', 
    '__reduce_ex__', '__replace__', '__repr__', '__repr_args__', '__repr_name__', '__repr_recursion__', '__repr_str__', '__rich_repr__', '__setattr__', 
    '__setstate__', '__signature__', '__sizeof__', '__slots__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_calculate_keys', '_copy_and_set_values', '_get_value', '_iter', '_setattr_handler', 'ab_test_id', 'ab_test_variant_id', 'applied_rules', 'around_lat_lng', 'around_lat_lng_validate_regular_expression', 'automatic_insights', 'automatic_radius', 'construct', 'copy', 'dict', 'exhaustive', 'exhaustive_facets_count', 'exhaustive_nb_hits', 'exhaustive_typo', 'facets', 'facets_stats', 'from_dict', 'from_json', 'from_orm', 'hits', 'hits_per_page', 'index', 'index_used', 'json', 'message', 'model_computed_fields', 
    'model_config', 'model_construct', 'model_copy', 'model_dump', 'model_dump_json', 'model_extra', 'model_fields', 'model_fields_set', 'model_json_schema', 
    'model_parametrized_name', 'model_post_init', 'model_rebuild', 'model_validate', 'model_validate_json', 'model_validate_strings', 'nb_hits', 'nb_pages', 
    'nb_sorted_hits', 'page', 'params', 'parse_file', 'parse_obj', 'parse_raw', 'parsed_query', 'processing_time_ms', 'processing_timings_ms', 'query', 
    'query_after_removal', 'query_id', 'redirect', 'rendering_content', 'schema', 'schema_json', 'server_time_ms', 'server_used', 'to_dict', 'to_json', 
    'update_forward_refs', 'user_data', 'validate']
