def login():
    ds = DarwinSdk()
    ds.set_url('https://amb-demo-api.sparkcognition.com/v1#/')
    status, msg = ds.auth_login_user('em.j.reinhart@gmail.com', 'xeyW2ue46p')

    if not status:
        print(msg)
