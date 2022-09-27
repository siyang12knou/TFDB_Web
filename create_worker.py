from datetime import date

from sqlmodel.ext.asyncio.session import AsyncSession

from model.user import User
from service.user import save_user


async def init_worker(session: AsyncSession):
    users: list = [
        User(id="이재성", name="이재성", password="01049215660", tel="010-4921-5660", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김태연", name="김태연", password="01087655849", tel="010-8765-5849", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최효빈", name="최효빈", password="01094451645", tel="010-9445-1645", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="정세진", name="정세진", password="01087783987", tel="010-8778-3987", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김재은", name="김재은", password="01079978786", tel="010-7997-8786", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="제명숙", name="제명숙", password="01076644742", tel="010-7664-4742", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최보윤", name="최보윤", password="01024372863", tel="010-2437-2863", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최은서", name="최은서", password="01020131868", tel="010-2013-1868", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최정분", name="최정분", password="01025898254", tel="010-2589-8254", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김종숙", name="김종숙", password="01054301826", tel="010-5430-1826", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="안래희", name="안래희", password="01023064112", tel="010-2306-4112", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이영숙", name="이영숙", password="01097004112", tel="010-9700-4112", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="오희영", name="오희영", password="01053930418", tel="010-5393-0418", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이수진", name="이수진", password="01085787243", tel="010-8578-7243", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이설아", name="이설아", password="01022840064", tel="010-2284-0064", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="강미현", name="강미현", password="01092617467", tel="010-9261-7467", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-08-31")),
        User(id="김강훈", name="김강훈", password="01097982745", tel="010-9798-2745", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박민규", name="박민규", password="01082183639", tel="010-8218-3639", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="손민이", name="손민이", password="01065489810", tel="010-6548-9810", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="심혜원", name="심혜원", password="01036890973", tel="010-3689-0973", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="안철민", name="안철민", password="01022869632", tel="010-2286-9632", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-07-31")),
        User(id="장지수", name="장지수", password="01042706953", tel="010-4270-6953", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="임지우", name="임지우", password="01091977801", tel="010-9197-7801", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="정준하", name="정준하", password="01026764440", tel="010-2676-4440", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="양우혁", name="양우혁", password="01050621832", tel="010-5062-1832", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박찬하", name="박찬하", password="01075035342", tel="010-7503-5342", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="안원희", name="안원희", password="01094849759", tel="010-9484-9759", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김재원", name="김재원", password="01048193540", tel="010-4819-3540", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김채원", name="김채원", password="01079376423", tel="010-7937-6423", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="윤수연", name="윤수연", password="01077097460", tel="010-7709-7460", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박규빈", name="박규빈", password="01048133975", tel="010-4813-3975", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="장재원", name="장재원", password="01064082335", tel="010-6408-2335", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="화희중", name="화희중", password="01039561676", tel="010-3956-1676", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김준제", name="김준제", password="01027658160", tel="010-2765-8160", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최소은", name="최소은", password="01020362581", tel="010-2036-2581", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이서현", name="이서현", password="01087622242", tel="010-8762-2242", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박효진", name="박효진", password="01022872281", tel="010-2287-2281", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="정현정", name="정현정", password="01054676078", tel="010-5467-6078", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-07-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이영주", name="이영주", password="01092061060", tel="010-9206-1060", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="문의종", name="문의종", password="01058135453", tel="010-5813-5453", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="설민규", name="설민규", password="01083053665", tel="010-8305-3665", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최지호", name="최지호", password="01020307755", tel="010-2030-7755", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김찬",  name="김찬",  password="01050670241", tel="010-5067-0241", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="강채림", name="강채림", password="01045838710", tel="010-4583-8710", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="송찬주", name="송찬주", password="01055280163", tel="010-5528-0163", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="임영신", name="임영신", password="01086700195", tel="010-8670-0195", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-08-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="송서윤", name="송서윤", password="01065583299", tel="010-6558-3299", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="신요한", name="신요한", password="01067257144", tel="010-6725-7144", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="배서림", name="배서림", password="01097439911", tel="010-9743-9911", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="안성은", name="안성은", password="01041783265", tel="010-4178-3265", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="이은혜", name="이은혜", password="01099058335", tel="010-9905-8335", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김향화", name="김향화", password="01072211379", tel="010-7221-1379", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김주영", name="김주영", password="01072259967", tel="010-7225-9967", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김하늘", name="김하늘", password="01094002620", tel="010-9400-2620", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="유지혜", name="유지혜", password="01062593314", tel="010-6259-3314", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="조주현", name="조주현", password="01024199946", tel="010-2419-9946", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김예지", name="김예지", password="01090874269", tel="010-9087-4269", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="조은송", name="조은송", password="01024666590", tel="010-2466-6590", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="강정운", name="강정운", password="01030645406", tel="010-3064-5406", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="안지민", name="안지민", password="01025337757", tel="010-2533-7757", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="허지은", name="허지은", password="01039317035", tel="010-3931-7035", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김영미", name="김영미", password="01036884645", tel="010-3688-4645", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김소영", name="김소영", password="01087776713", tel="010-8777-6713", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="최영랑", name="최영랑", password="01088816609", tel="010-8881-6609", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김엘림", name="김엘림", password="01037609337", tel="010-3760-9337", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="정현애", name="정현애", password="01062327093", tel="010-6232-7093", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김채은", name="김채은", password="01096269005", tel="010-9626-9005", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김나형", name="김나형", password="01032325447", tel="010-3232-5447", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="유민혁", name="유민혁", password="01056966896", tel="010-5696-6896", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="황경옥", name="황경옥", password="01033686896", tel="010-3368-6896", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="송재희", name="송재희", password="01039281426", tel="010-3928-1426", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="조현지", name="조현지", password="01098360806", tel="010-9836-0806", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박희민", name="박희민", password="01056923905", tel="010-5692-3905", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="유보람", name="유보람", password="01049857882", tel="010-4985-7882", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="김도희", name="김도희", password="01044491843", tel="010-4449-1843", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="황주은", name="황주은", password="01031437113", tel="010-3143-7113", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="박병준", name="박병준", password="01084627949", tel="010-8462-7949", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
        User(id="서제인", name="서제인", password="01044729975", tel="010-4472-9975", email="", role="[\"TFDB_WORKER\"]", contract_start_date=date.fromisoformat("2022-09-01"), contract_end_date=date.fromisoformat("2022-11-30")),
    ]
    for user in users:
        await save_user(user, session=session)
