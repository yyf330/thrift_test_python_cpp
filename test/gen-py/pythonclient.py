
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import sys, glob
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])

from checklicense import ProcessCheckL 
from checklicense.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = ProcessCheckL.Client(protocol)

    # Connect!
    transport.open()

    try:
        #u1 = ProcessCheckL()  
        #u1.id=2  
        #u1.name='nick'  
        #u1.blurb='test bbb'  
        #client.store(u1) 
        returnval=client.CheckLicense() 
        print 'returnval=',returnval
    #    print 'store done!'
    except InvalidOperation, io: 
        print 'InvalidOperation: %r' % io


    #u = client.getUser(456)  
    #print 'id=%s name=%s blurb=%s' %(u.id,u.name,u.blurb)

    # Close!
    transport.close()

except Thrift.TException, tx:
    print '%s' % (tx.message)
