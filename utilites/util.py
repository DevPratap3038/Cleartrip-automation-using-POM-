class Utils:
    def Assertion_utils_for_assending(self, list):
        for i in range(len(list)):
            # print(list[i].text)
            assert list[i].text <= list[i+1].text


    def print_list_elements(self, list_name):
        for ele in list_name:
            print(ele.text)
