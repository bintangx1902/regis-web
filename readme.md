# To Do list

## Backend

| #  | Job Desk         | Done |
|----|------------------|------|
| 1. | Login            |      |
| 2. | Register         |      |
| 3. | Forgot Password  |      |
| 4. | Landing Page     |      |
| 5. | Isi Nilai Rapor  |      |
| 6. | Daftar Mahasiswa |      |
|    | &nbsp;           |      |

## Frontend
| #  | Job Desk         | Done |
|----|------------------|------|
| 1. | Login            |      |
| 2. | Register         |      |
| 3. | Forgot Password  |      |
| 4. | Landing Page     |      |
| 5. | Isi Nilai Rapor  |      |
| 6. | Daftar Mahasiswa |      |
|    | &nbsp;           |      |


accounts/ login/ [name='account_login']
accounts/ logout/ [name='account_logout']
accounts/ inactive/ [name='account_inactive']
accounts/ signup/ [name='account_signup']
accounts/ reauthenticate/ [name='account_reauthenticate']
accounts/ email/ [name='account_email']
accounts/ confirm-email/ [name='account_email_verification_sent']
accounts/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
accounts/ password/change/ [name='account_change_password']
accounts/ password/set/ [name='account_set_password']
accounts/ password/reset/ [name='account_reset_password']
accounts/ password/reset/done/ [name='account_reset_password_done']