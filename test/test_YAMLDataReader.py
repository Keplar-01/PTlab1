# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


class TestYAMLDataReader:

    @pytest.fixture()
    def yaml_file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = "- Иванов Константин Дмитриевич:\n" + \
                       "    математика: 91\n" + "    химия: 100\n" + \
                       "- Петров Петр Семенович:\n" + \
                       "    русский язык: 87\n" + "    литература: 78\n"

        expected_data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return yaml_content, expected_data

    @pytest.fixture()
    def filepath_and_data(self,
                          yaml_file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(yaml_file_and_data_content[0], encoding='utf-8')
        return str(p), yaml_file_and_data_content[1]

    def test_yaml_read(self,
                       filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
