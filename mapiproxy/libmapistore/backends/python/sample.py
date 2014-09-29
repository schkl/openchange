#!/usr/bin/python
# OpenChange python sample backend
#
# Copyright (C) Julien Kerihuel <j.kerihuel@openchange.org> 2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os,sys

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.sep.join((root, '..', '..')))

import json
import uuid
from datetime import datetime
from openchange import mapistore

class BackendObject(object):

    name = "sample"
    description = "Sample backend"
    namespace = "sample://"

    def __init__(self):
        print '[PYTHON]: %s backend class __init__' % self.name
        return

    def init(self):
        """ Initialize sample backend
        """
        print '[PYTHON]: %s backend.init: init()' % self.name
        return 0

    def list_contexts(self, username):
        """ List context capabilities of this backend.
        """
        print '[PYTHON]: %s backend.list_contexts(): username = %s' % (self.name, username)
        deadbeef = {}
        deadbeef["url"] = "sample://deadbeef0000001/"
        deadbeef["name"] = "deadbeef"
        deadbeef["main_folder"] = True
        deadbeef["role"] = mapistore.ROLE_MAIL
        deadbeef["tag"] = "tag"

        contexts = [deadbeef,]
        return contexts

    def create_context(self, uri):
        """ Create a context.
        """

        print '[PYTHON]: %s backend.create_context: uri = %s' % (self.name, uri)
        context = ContextObject()

        return (0, context)


class ContextObject(BackendObject):

    mapping = {}

    def __init__(self):

        # Attachments
        attachment1 = {}
        attachment1["properties"] = {}
        attachment1["properties"]["PidTagMid"] = 0xdead00010000001
        attachment1["properties"]["PidTagAttachNumber"] = 0
        attachment1["properties"]["PidTagAttachMethod"] = 1
        attachment1["properties"]["PidTagAttachmentLinkId"] = 0x0
        attachment1["properties"]["PidTagAttachmentHidden"] = False
        attachment1["properties"]["PidTagAttachFilename"] = "Dummyfile.txt"
        attachment1["properties"]["PidTagAttachLongFilename"] = "Long Dummyfile.txt"
        attachment1["properties"]["PidTagAttachLongPathname"] = "Long Dummyfile.txt"
        attachment1["properties"]["PidTagAttachPathname"] = "Dummyfile.txt"
        attachment1["properties"]["PidTagAttachExtension"] = "txt"
        attachment1["properties"]["PidTagAttachContentId"] = "Content Id"
        attachment1["properties"]["PidTagAttachRendering"] = 1
        attachment1["properties"]["PidTagAttachDataBinary"] = bytearray("<html><head></head><h1>Attach me</h1></body></html>")
        attachment1["properties"]["PidTagAttachSize"] = len(attachment1["properties"]["PidTagAttachDataBinary"])

        # Recipients
        DummyTo = {}
        DummyTo["PidTagRecipientType"] = 0x1
        DummyTo["PidTagSmtpAddress"] = "dummy@openchange.org"
        DummyTo["PidTagRecipientDisplayName"] = "Dummy User"
        DummyTo["PidTagSentRepresentingName"] = "Dummy User"
        DummyTo["PidTagDisplayTo"] = "dummy@openchange.org"

        message1 = {}
        message1["recipients"] = [DummyTo, ]
        message1["attachments"] = [attachment1, ]
        message1["mid"] = 0xdead00010000001
        message1["fai"] = False
        message1["cache"] = {}
        message1["properties"] = {}
        message1["properties"]["PidTagFolderId"] = 0xdeadbeef0000001
        message1["properties"]["PidTagMid"] = message1["mid"]
        message1["properties"]["PidTagInstID"] =  message1["mid"]
        message1["properties"]["PidTagSubjectPrefix"] = "Re:"
        message1["properties"]["PidTagInstanceNum"] = 0
        message1["properties"]["PidTagRowType"] = 1
        message1["properties"]["PidTagDepth"] = 0
        message1["properties"]["PidTagMessageClass"] = "IPM.Note"
        message1["properties"]["PidTagSubject"] = "Dummy Sample Email"
        message1["properties"]["PidTagNormalizedSubject"] = message1["properties"]["PidTagSubject"]
        message1["properties"]["PidTagConversationTopic"] = message1["properties"]["PidTagSubject"]
        message1["properties"]["PidTagBody"] = "This is the content of this sample email"
        message1["properties"]["PidTagHtml"] = bytearray("<html><head></head><h1>"+ message1["properties"]["PidTagBody"] + "</h1></body></html>")
        message1["properties"]["PidTagImportance"] = 2
        message1["properties"]["PidTagSensitivity"] = 1
        message1["properties"]["PidTagHasAttachments"] = True
        message1["properties"]["PidTagContentCount"] = len(message1["attachments"])
        message1["properties"]["PidTagInternetMessageId"] = "internet-message-id@openchange.org"
        message1["properties"]["PidTagChangeKey"] = bytearray(uuid.uuid1().bytes + '\x00\x00\x00\x00\x00\x01')
        message1["properties"]["PidTagMessageStatus"] = 0
        message1["properties"]["PidTagMessageFlags"] = 0
        message1["properties"]["PidTagLastModificationTime"] = float(datetime.now().strftime("%s.%f"))
        message1["properties"]["PidTagMessageDeliveryTime"] = float(datetime.now().strftime("%s.%f"))

        subfolder = {}
        subfolder["uri"] = "sample://deadbeef0000001/dead0010000001/"
        subfolder["fid"] = 0xdead10010000001
        subfolder["subfolders"] = []
        subfolder["messages"] = []
        subfolder["properties"] = {}
        subfolder["properties"]["PidTagParentFolderId"] = 0xdeadbeef0000001
        subfolder["properties"]["PidTagFolderId"] = subfolder["fid"]
        subfolder["properties"]["PidTagFolderType"] = 1
        subfolder["properties"]["PidTagDisplayName"] = "DEAD-1001"
        subfolder["properties"]["PidTagContainerClass"] = "IPF.Note"
        subfolder["properties"]["PidTagDefaultPostMessageClass"] = "IPM.Note"
        subfolder["properties"]["PidTagSubfolders"] = False
        subfolder["properties"]["PidTagAttributeHidden"] = False
        subfolder["properties"]["PidTagComment"] = "WALKING COMMENT"
        subfolder["properties"]["PidTagContentCount"] = len(subfolder["messages"])
        subfolder["properties"]["PidTagContentUnreadCount"] = len(subfolder["messages"])
        subfolder["properties"]["PidTagChildFolderCount"] = len(subfolder["subfolders"])
        subfolder["cache"] = {}
        subfolder["cache"]["properties"] = {}
        subfolder["cache"]["messages"] = []

        self.mapping[0xdeadbeef0000001] = {}
        self.mapping[0xdeadbeef0000001]["uri"] = "sample://deadbeef0000001/"
        self.mapping[0xdeadbeef0000001]["properties"] = {}
        self.mapping[0xdeadbeef0000001]["properties"]["PidTagFolderId"] = 0xdeadbeef0000001
        self.mapping[0xdeadbeef0000001]["cache"] = {}
        self.mapping[0xdeadbeef0000001]["subfolders"] = [subfolder, ]
        self.mapping[0xdeadbeef0000001]["messages"] = [message1, ]

        print '[PYTHON]: %s context class __init__' % self.name
        return

    def get_path(self, fmid):
        print '[PYTHON]: %s context.get_path' % self.name
        if fmid in self.mapping:
            print '[PYTHON]: %s get_path URI: %s' % (self.name, self.mapping[fmid]["uri"])
            return self.mapping[fmid]["uri"]
        else:
            print '[Python]: %s get_path URI: None' % (self.name)
            return None

    def get_root_folder(self, folderID):
        print '[PYTHON]: %s context.get_root_folder' % self.name
        folder = FolderObject(self.mapping[folderID], None, folderID, 0x0)
        return (0, folder)


class FolderObject(ContextObject):

    def __init__(self, basedict, parentdict, folderID, parentFID):
        print '[PYTHON]: %s folder.__init__(fid=%s)' % (self.name, folderID)
        self.basedict = basedict
        self.parentdict = parentdict
        self.parentFID = parentFID;
        self.folderID = folderID;
        return

    def open_folder(self, folderID):
        print '[PYTHON]: %s folder.open_folder(0x%x)' % (self.name, folderID)

        for item in self.basedict["subfolders"]:
            if str(item["fid"]) == str(folderID):
                print '[PYTHON]: folderID 0x%x found\n' % (folderID)
                return FolderObject(item, self.basedict, folderID, self.folderID)
        return None

    def create_folder(self, properties, folderID):
        print '[PYTHON]: %s folder.create_folder(%s)' % (self.name, folderID)
        j = json.dumps(properties, indent=4)
        print '[PYTHON]: %s ' % j

        folder = {}
        folder["uri"] = "%s/0x%x" % (self.basedict["uri"], folderID)
        folder["fid"] = folderID
        folder["properties"] = {}
        folder["properties"]["PidTagFolderId"] = folder["fid"]
        if properties.has_key("PidTagDisplayName"):
            folder["properties"]["PidTagDisplayName"] = properties["PidTagDisplayName"]
        if properties.has_key("PidTagComment"):
            folder["properties"]["PidTagComment"] = properties["PidTagComment"]
        folder["subfolders"] = []
        folder["messages"] = []
        folder["cache"] = {}
        folder["cache"]["properties"] = {}
        folder["cache"]["messages"] = []

        self.basedict["subfolders"].append(folder)

        return (0, FolderObject(folder, self.basedict, folderID, self.folderID))

    def delete(self):
        print '[PYTHON]: %s folder.delete(%s)' % (self.name, self.folderID)
        for item in self.parentdict["subfolders"]:
            if str(item["fid"]) == str(self.folderID):
                self.parentdict["subfolders"].remove(item)
                return 0
        return 17

    def open_table(self, table_type):
        print '[PYTHON]: %s folder.open_table' % (self.name)
        table = TableObject(self, table_type)
        return (table, self.get_child_count(table_type))

    def get_child_count(self, table_type):
        print '[PYTHON]: %s folder.get_child_count' % (self.name)
        counter = { 1: self._count_folders,
                    2: self._count_messages,
                    3: self._count_zero,
                    4: self._count_zero,
                    5: self._count_zero,
                    6: self._count_zero
                }
        return counter[table_type]()

    def _count_folders(self):
        print '[PYTHON][INTERNAL]: %s folder._count_folders(0x%x): %d' % (self.name, self.folderID, len(self.basedict["subfolders"]))
        return len(self.basedict["subfolders"])

    def _count_messages(self):
        print '[PYTHON][INTERNAL]: %s folder._count_messages(0x%x): %d' % (self.name, self.folderID, len(self.basedict["messages"]))
        return len(self.basedict["messages"])

    def _count_zero(self):
        return 0

    def open_message(self, mid, rw):
        print '[PYTHON]: %s folder.open_message()' % self.name

        for item in self.basedict["messages"]:
            if str(item["mid"]) == str(mid):
                print '[PYTHON]: messageID 0x%x found\n' % (mid)
                return MessageObject(item, self, mid, rw)
        return None

    def create_message(self, mid, associated):
        print '[PYTHON]: %s folder.create_message()' % self.name
        newmsg = {}
        newmsg["recipients"] = []
        newmsg["attachments"] = []
        newmsg["mid"] = mid
        newmsg["fai"] = associated
        newmsg["cache"] = {}
        newmsg["properties"] = {}
        newmsg["properties"]["PidTagMessageId"] = newmsg["mid"]
        self.basedict["cache"]["messages"].append(newmsg)
        return MessageObject(newmsg, self, mid, 1)

    def get_properties(self, properties):
        print '[PYTHON]: %s folder.get_properties()' % (self.name)
        print properties
        return self.basedict["properties"]

    def set_properties(self, properties):
        print '[PYTHON]: %s folder.set_properties()' % (self.name)

        tmpdict = self.basedict["cache"].copy()
        tmpdict.update(properties)
        self.basedict["cache"] = tmpdict

        print self.basedict["cache"]
        return 0

class TableObject(BackendObject):

    def __init__(self, folder, tableType):
        print '[PYTHON]: %s table.__init__()' % (self.name)
        self.folder = folder
        self.tableType = tableType
        self.properties = []
        return

    def set_columns(self, properties):
        print '[PYTHON]: %s table.set_columns()' % (self.name)
        self.properties = properties
        print 'properties: [%s]\n' % ', '.join(map(str, self.properties))
        return 0

    def get_row(self, rowId, query_type):
        print '[PYTHON]: %s table.get_row()' % (self.name)

        rowdata = None
        if self.tableType == 1:
            subfolders = self.folder.basedict["subfolders"]
            if (len(subfolders) > rowId and
                subfolders[rowId] and
                subfolders[rowId].has_key("properties")):
                rowdata = subfolders[rowId]["properties"]
        elif self.tableType == 2:
            messages = self.folder.basedict["messages"]
            if (len(messages) > rowId and
                messages[rowId] and
                messages[rowId].has_key("properties")):
                rowdata = messages[rowId]["properties"]
        elif self.tableType == 5:
            attachments = self.folder.message["attachments"]
            if (len(attachments) > rowId and
                attachments[rowId] and
                attachments[rowId].has_key("properties")):
                rowdata = attachments[rowId]["properties"]
        return (self.properties, rowdata)


    def get_row_count(self, query_type):
        print '[PYTHON]: %s table.get_row_count()' % (self.name)
        return self.folder.get_child_count(self.tableType)

class MessageObject(BackendObject):

    def __init__(self, message, folder, mid, rw):
        print '[PYTHON]: %s message.__init__()' % (self.name)
        self.folder = folder
        self.message = message
        self.mid = mid
        self.rw = rw

        return

    def get_message_data(self):
        print '[PYTHON]: %s message.get_message_data()' % (self.name)
        return (self.message["recipients"], self.message["properties"])

    def get_properties(self, properties):
        print '[PYTHON]: %s message.get_properties()' % (self.name)
        return self.message["properties"]

    def set_properties(self, properties):
        print '[PYTHON]: %s message.set_properties()' % (self.name)

        tmpdict = self.message["cache"].copy()
        tmpdict.update(properties)
        self.message["cache"] = tmpdict;

        print self.message["cache"]
        return 0

    def save(self):
        print '[PYTHON]: %s message.save()' % (self.name)

        for item in self.folder.basedict["cache"]["messages"]:
            if str(item["mid"]) == str(self.mid):
                self.folder.basedict["messages"].append(item)
                self.folder.basedict["cache"]["messages"].remove(item)
                return 0
        return 17

    def _count_attachments(self):
        print '[PYTHON][INTERNAL]: %s message._count_folders(0x%x): %d' % (self.name, self.mid, len(self.message["attachments"]))
        return len(self.message["attachments"])

    def get_child_count(self, table_type):
        print '[PYTHON]: %s message.get_child_count' % (self.name)
        counter = { 5: self._count_attachments }
        return counter[table_type]()

    def open_attachment(self, attach_id):
        print '[PYTHON]: %s message.open_attachment(): %d/%d' % (self.name, attach_id,
                                                                 len(self.message["attachments"]))
        if attach_id > len(self.message["attachments"]):
            return None
        return AttachmentObject(self.message["attachments"][attach_id], self, attach_id)


    def get_attachment_table(self):
        print '[PYTHON]: %s message.get_attachment_table()' % (self.name)
        table = TableObject(self, 5)
        return (table, self.get_child_count(5))


class AttachmentObject(BackendObject):

    def __init__(self, attachment, message, attachid):
        print '[PYTHON]: %s attachment.__init__()' % (self.name)
        print attachment
        self.attachment = attachment
        self.message = message
        self.attachid = attachid
        return

    def get_properties(self, properties):
        print '[PYTHON]: %s message.get_properties()' % (self.name)
        return self.attachment["properties"]