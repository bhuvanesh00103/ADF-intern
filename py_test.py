'''Importing required modules'''
import pytest
from main import StringManipulate

class Test:
    '''Test Class'''
    obj = StringManipulate('input', 'output')
    def test_prefix1(self):
        '''Test Prefix method'''
        assert self.obj.prefix_as_to() == 3

    @pytest.mark.xfail
    def test_prefix2(self):
        '''Test Prefix method'''
        assert self.obj.prefix_as_to() == 4

    def test_suffix1(self):
        '''Test suffix method'''
        assert self.obj.ending_with_ing() == 3

    @pytest.mark.xfail
    def test_suffix2(self):
        '''Test suffix method'''
        assert self.obj.ending_with_ing() == 6

    def test_max_repeat1(self):
        '''Test max repeat method'''
        assert self.obj.word_max_repeat() == 'non'

    @pytest.mark.xfail
    def test_max_repeat2(self):
        '''Test max repeat method'''
        assert self.obj.word_max_repeat() == 'hello'

    def test_palindrome1(self):
        '''Test Palin method'''
        lst = self.obj.palindrome_words()
        assert lst[2:6] == ['esse', 'a', 'a', 'a']
        assert lst[:3] == ['non', 'non', 'esse']

    @pytest.mark.skip
    def test_palindrome2(self):
        '''Test Palin method'''
        assert self.obj.palindrome_words()[:3] == ['non', 'non', 'esse']

    @pytest.mark.xfail
    def test_palindrome3(self):
        '''Test Palin method'''
        assert self.obj.palindrome_words()[:3] == [ 'non', 'esse']

    def test_unique_words1(self):
        '''Test unique words method'''
        lst = self.obj.find_unique_words()
        assert 'naturam' in lst and 'lex' in lst

    @pytest.mark.xfail
    def test_unique_words2(self):
        '''Test unique words method'''
        lst = self.obj.find_unique_words()
        assert 'hello' in lst and 'lex' in lst

    def test_word_dict1(self):
        '''Test word dict method'''
        dict1 = self.obj.word_dict()
        assert len(dict1) == 546

    @pytest.mark.xfail
    def test_word_dict2(self):
        '''Test word dict method'''
        dict1 = self.obj.word_dict()
        assert dict1[10] == 'Hello'
