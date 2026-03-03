Enterasys MIB Support

Industry Standard MIB Support

The Enterasys corporate strategy for SNMP Management is to support a
wide range of IETF and IEEE standard MIB modules, so that our products
are easily managed using third party SNMP applications. 

Management information is viewed as a collection of managed objects,
residing in a virtual information store, termed the Management
Information Base (MIB). Collections of related objects are defined
in MIB modules. 

The MIB modules supported in each product, and the associated document,
are listed in the release notes for the product, available at
http://www.enterasys.com/support/relnotes/. 

IETF MIB modules are available at http://www.ietf.org/rfc.html.
IEEE MIB modules are appended to the standard they are designed
to manage, which are available at http://standards.ieee.org/getieee802/.
These and other standard MIBS are available from the standards
subdirectory located within this directory.

Enterprise MIB Modules

When designing SNMP, the IETF recognized that the release of
functionality in products often precedes the availability of an
industry standard MIB module, and provided for the development of
enterprise-specific MIB modules.

When no industry-standard MIB module exists to manage the functionality
present in our products, Enterasys designs enterprise-specific MIBs to
make our products manageable. It is our corporate strategy to help the
IETF and IEEE develop MIB module standards for emerging technologies and
to migrate away from enterprise-specific MIBs once a comparable standard 
has been established.

The enterprise-specific MIB modules used in our products are listed in
the release notes for the products, and are available for download from
various subdirectories within this directory.

How to Import MIB Modules

If you have downloaded more recent firmware to support new features and
bug fixes for products, and are having problems managing the device, you
may need to import (compile) the current MIB files into your network
management application's MIB database. For Enterasys network management
products, consult the documentation to determine the procedure for 
importing MIBs. 

Note that all Enterasys MIB modules are compliant to the IETF SMIv2
standard. Older applications which do not support the current SMI
standard may not be able to easily or completely import SMIv2-compliant
MIB modules.

