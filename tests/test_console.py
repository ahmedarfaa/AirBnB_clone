#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Base class for testing Console.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)


class TestBaseModel(unittest.TestCase):
    """Testing `Basemodel `commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ife"')
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(f'update BaseModel {b1.id} age 25')
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {b1.id} savings 35.89')
            self.assertIn("savings", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'update BaseModel {b1.id} age 10 color "green"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestBaseModelDotNotation(unittest.TestCase):
    """Testing `Basemodel `commands using dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'BaseModel.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test count basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, name, "Ife")'))
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, age, 25)'))
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'BaseModel.update({b1.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_update_basemodel_dict(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            cmmd = f'BaseModel.update({b1.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(b1.__dict__["age"], 25)
            self.assertIsInstance(b1.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy({bm.id})'))
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestUser(unittest.TestCase):
    """Testing the `user` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)
