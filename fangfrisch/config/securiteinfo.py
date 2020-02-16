"""
Copyright © 2020 Ralph Seichter

This file is part of "Fangfrisch".

Fangfrisch is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Fangfrisch is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Fangfrisch. If not, see <https://www.gnu.org/licenses/>.
"""
from fangfrisch.config import MAX_AGE
from fangfrisch.config import PREFIX

securiteinfo = {
    'securiteinfo': {
        'customer_id': 'you_forgot_to_configure_customer_id',
        MAX_AGE: '720',  # String representation of max age (in minutes)
        PREFIX: 'https://www.securiteinfo.com/get/signatures/${customer_id}/',
        'url_android': f'${{{PREFIX}}}securiteinfoandroid.hdb',
        'url_ascii': f'${{{PREFIX}}}securiteinfoascii.hdb',
        'url_html': f'${{{PREFIX}}}securiteinfohtml.hdb',
        'url_javascript': f'${{{PREFIX}}}javascript.ndb',
        'url_old': f'${{{PREFIX}}}securiteinfoold.hdb',
        'url_pdf': f'${{{PREFIX}}}securiteinfopdf.hdb',
        'url_securiteinfo': f'${{{PREFIX}}}securiteinfo.hdb',
        'url_securiteinfo_ign2': f'${{{PREFIX}}}securiteinfo.ign2',
        'url_spam_marketing': f'${{{PREFIX}}}spam_marketing.ndb',
    }
}
