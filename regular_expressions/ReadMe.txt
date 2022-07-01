
                 "Python Regular Expressions"
=================================================================

Python Support Regular Expressions with "re module"

re module has lot of inbuilt functions,

            1. re.search(pattern, string)
                    
                    output: 
                        Success : <re.Match object; span=(start_position, end_position), match='portal'> 
                        Failure : None

            re.search(pattern, string).start()  / re.search(pattern, string).end()
            
            2. re.findall('pattern', string)

                output:
                    Success : ['value', 'value', 'value']
                    Failure : ['']
            
            3. re.compile()


Note:- Best Platform to learn and pratice regular expression https://regex101.com/