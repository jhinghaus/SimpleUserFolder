# Copyright (c) 2001 New Information Paradigms Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.
#
# $Id: dummyUserSource.py,v 1.1.4.2 2003/08/05 17:24:30 chrisw Exp $

import Zope

from Acquisition import Implicit

from Products.SimpleUserFolder.SimpleUserFolder import SimpleUserFolder

class User:

    def __init__(self,password,roles):
        self.password = password
        self.roles = roles

class dummyUserSource(Implicit):

    def __init__(self):
        # setup the user registry
        self.users = {'test_user':User('password',
                                       [])}

    def __getitem__(self,name):
        return self.users[name]

    def addUser(self,name, password, roles):
        """add a user"""
        if self.users.has_key(name):
            raise ValueError
        self.users[name] = User(password,roles)

    def editUser(self,name, password, roles):
        """edit a user"""
        user = self.users[name]
        user.password = password
        user.roles = roles

    def getUserNames(self):
        """return a list of usernames"""
        names = self.users.keys()
        names.sort()
        return names

    def getUserDetails(self,name):
        """return a dictionary for the specified user"""        
        if self.users.has_key(name):
            # nice hack, return the dict from the object
            return self.users[name].__dict__
        return None

    def deleteUser(self,name):
        """delete the specified user"""
        del self.users[name]

class dummyUserFolder(SimpleUserFolder):

    def __init__(self):
        # setup the user registry
        self.users = {'test_user':User('password',
                                       [])}

    def __getitem__(self,name):
        return self.users[name]

    def addUser(self,name, password, roles):
        """add a user"""
        if self.users.has_key(name):
            raise ValueError
        self.users[name] = User(password,roles)

    def editUser(self,name, password, roles):
        """edit a user"""
        user = self.users[name]
        user.password = password
        user.roles = roles

    def getUserNames(self):
        """return a list of usernames"""
        names = self.users.keys()
        names.sort()
        return names

    def getUserDetails(self,name):
        """return a dictionary for the specified user"""        
        if self.users.has_key(name):
            # nice hack, return the dict from the object
            return self.users[name].__dict__
        return None

    def deleteUser(self,name):
        """delete the specified user"""
        del self.users[name]
    
    
    
