from dataclasses import dataclass
from typing import Protocol,Type
from src.extractor import *
from src.transformer import *
from src.loader import *



@dataclass
class ETL:
    extractor: Extractor
    transformer: Transformer
    loader: Loader

    def run(self):
        """
        E then T then L
        """

        records = self.extractor.extract()
        transformed = self.transformer.transform(records)
        self.loader.load(transformed)

@dataclass
class ETLFactory:
    extractor_class: Type[Extractor]
    transformer_class: Type[Transformer]
    loader_class: Type[Loader]

    def __call__(self,config) -> ETL:
        return ETL(
            self.extractor_class(config),
            self.transformer_class(config), 
            self.loader_class(config),
        )
    

def get_factory(source_name):

    FACTORIES = {
        "source1": ETLFactory(csvExtractor, sourceOneTransformer,MySQLLoader),
        "source2": ETLFactory(csvExtractor, sourceTwoTransformer,MySQLLoader),
        "source3": ETLFactory(csvExtractor, sourceThreeTransformer,MySQLLoader),
    }

    return  FACTORIES[source_name]
