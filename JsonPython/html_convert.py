#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GOLF
#
# Created:     19/09/2014
# Copyright:   (c) GOLF 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def tagconvert(param):
    tag_sTD="<td>"
    tag_eTD="</td>"
    return tag_sTD + param + tag_eTD

def selectcombobox(paramvalue,paramtitle):
    text=''
    if '' != paramtitle:
        if ''!= paramvalue:
            text = text + '<option '
            text = text + 'value="'
            text = text + paramvalue
            text = text + '">'
            text = text + paramtitle
            text = text + '</option>'
    return text
