# this is pending : 
import textwrap


# def wrap(string, max_width):
#     for i in string:
#         l=len(string)
#         if (l==max_width):
#             print("\n")
    
    

# if __name__ == '__main__':
#     string, max_width = input("Enter the string : "), int(input("Enter the number : "))
#     result = wrap(string, max_width)
#     print(result)



# this is right solution for above code : 
def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))    

if __name__ == '__main__':
    string, max_width = input("Enter the string : "), int(input("enter the number : "))
    result = wrap(string, max_width)
    print(result)