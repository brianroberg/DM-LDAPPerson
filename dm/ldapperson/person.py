class Person():
    """
    Test instantiation.
        >>> person = Person()
        >>> person.firstname
        'Joe'

    Test setting last name.
        >>> person.lastname
        'Staff'

    """
    
    def __init__(self):
        self.firstname = 'Joe'
        self.lastname = 'Staff'
        self.is_current_staff = True
        self.promotion_level = 'Intern Staff'

    def set_promotion_level(self, promotion_level):
        """
        Test setting promotion level.
            >>> person = Person()
            >>> person.promotion_level
            'Intern Staff'
            >>> person.set_promotion_level('Former Staff')
            >>> person.promotion_level
            'Former Staff'
        
        Setting promotion level to "Former Staff" should also change
        the is_current_staff flag.
            >>> person.is_current_staff
            False
        """
        
        self.promotion_level = promotion_level
        if promotion_level == 'Former Staff':
            self.is_current_staff = False