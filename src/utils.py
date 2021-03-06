import csv


class Utils:
    '''
        Esta classe tem a função de comportar funções utilitárias.
    '''

    def read_csv(self, document_path):
        '''

        :param document_path: String que contém o caminho relativo até o documento
        :return:
        '''
        file = []
        with open(document_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for column in reader:
                file.append(column)

        return file
    
    # Faz a organização das columas dentro do arquivo
    def transform_data_file(self, data):
        data_dict = {}
        for line in range(1, len(data)):
            data_dict.update( {(data[line][0], data[line][2]):
                                                    [data[line][0], data[line][1], data[line][2], data[line][3],
                                                    data[line][4], data[line][5], data[line][6], data[line][7]]} )
        return data_dict


