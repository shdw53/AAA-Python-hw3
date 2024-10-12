class CountVectorizer:
    """Класс для токенизации строк и подсчета терм-документной матрицы."""

    def __init__(self, lowercase: bool = True):
        """
        Инициализирует атрибуты класса.

        :lowercase: Показывает надо ли преобразовывать строку в нижний регистр
        """
        self.lowercase = lowercase

    def fit_transform(self, corpus: list) -> list:
        """
        Функция изучает список строк и возвращает терм-документную матрицу.

        :documents: Список из строк
        :return: Терм-документная матрица
        """
        if self.lowercase:
            self.corpus = [sentence.lower() for sentence in corpus]
        self.transformed_corpus = []
        self.feature_names = []

        if isinstance(self.corpus, list):
            for sentence in self.corpus:
                if isinstance(sentence, str):
                    self.feature_names += sentence.split()
                else:
                    raise ValueError(
                        "Input object consists of non-string values"
                    )
            self.feature_names = list(dict.fromkeys(self.feature_names))

            self.count_matrix = []
            for sentence in self.corpus:
                feature_counts = dict.fromkeys(self.feature_names)
                for word in feature_counts.keys():
                    feature_counts[word] = sentence.count(word)
                self.count_matrix.append(list(feature_counts.values()))
        else:
            raise ValueError("Input object is not iterable")

        return self.count_matrix

    def get_feature_names(self) -> list:
        """
        Возвращает уникальный список всех слов из введенного списка строк.

        :return: Уникальный список всех слов
        """
        return self.feature_names
