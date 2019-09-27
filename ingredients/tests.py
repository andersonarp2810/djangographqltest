# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import json

from graphene_django.utils.testing import GraphQLTestCase
from cookbook.schema import schema

class MyFancyTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            query {
                allCategories {
                    id
                    name
                    ingredients {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='allCategories'
        )

        #content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

    def test_query_with_variables(self):
        response = self.query(
            '''
            query {
                ingredient(id: $id) {
                    id
                    name
                }
            }
            ''',
            op_name='ingredient',
            variables={'id': 1}
        )

        #content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

