Inbox Influence
===============

A python library for interacting with the Influence Explorer Text API.

Usage:
------
Fetching entities from a string of text:

    >>>from inboxinfluence import inboxinfluence as ie
    >>>ie.apikey = 'mykey'
    >>>ie.contextualize('Some text that contains a name like barbara lee')
    [InboxInfluenceEntity({u'matched_text': [u'barbara lee'], u'entity_data': {u'held_seat': True, u'name': u'Barbara Lee', u'bioguide_id': None, u'raw_name': u'Barbara Lee (D)', u'upcoming_fundraisers': [{u'entertainment': u'Labor Breakfast', u'contributions_info': u'$5,000 Host; $2,500 Sponsor; $1,000 Patron', u'make_checks_payable_to': u'Barbara Lee for Congress', u'venue': u'Offices of The International Brotherhood of Teamsters', u'partytime_id': u'27703', u'start_date': u'2011-07-27', u'beneficiaries': [u'Rep. Barbara Lee (D, CA-9)'], u'hosts': [], u'start_time': u'08:30:00'}], u'seat_label': u'US House', u'affiliated_organizations': None, u'seat': u'federal:house', u'campaign_finance': {u'contributor_local_breakdown': {u'out_of_state': 500812.0, u'in_state': 2342438.0}, u'top_industries': [{u'amount': 545898.0, u'type': u'industry', u'id': u'b775d925e47f4648b1f1fd3e08625465', u'slug': u'employer-listed-but-category-unknown', u'name': u'Employer Listed But Category Unknown'}, {u'amount': 362479.0, u'type': u'industry', u'id': u'f50cf984a2e3477c8167d32e2b14e052', u'slug': u'lawyerslaw-firms', u'name': u'Lawyers/Law Firms'}, {u'amount': 281786.0, u'type': u'industry', u'id': u'7500030dffe24844aa467a75f7aedfd1', u'slug': u'real-estate', u'name': u'Real Estate'}, {u'amount': 262550.0, u'type': u'industry', u'id': u'e1fca6d984d24ea5abfe81abe87e46fb', u'slug': u'building-trade-unions', u'name': u'Building Trade Unions'}, {u'amount': 262550.0, u'type': u'industry', u'id': u'3f9486e3ea734801b0ec5de18040cfe8', u'slug': u'building-trades-unions', u'name': u'Building Trades Unions'}], u'recipient_breakdown': None, u'contributor_type_breakdown': {u'individual': 2843250.0, u'pac': 1783768.0}, u'contribution_total': 4627018.0}, u'crp_id': u'N00008046', u'lobbying': {u'is_lobbyist': None, u'expenditures': None, u'top_issues': None, u'is_lobbying_firm': None}, u'slug': u'barbara-lee', u'type': u'politician', u'id': u'6d1ec9c94ae748c6b86cc250761c6b13'}})]