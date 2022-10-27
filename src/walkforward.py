from collections import OrderedDict
from datetime import datetime
from datetime import timedelta
from typing import Union, Optional

from src.date import datetime2str


def _add_affixes(word: str, prefix: str, suffix: str):
    if prefix is not None:
        word = f"{prefix}__" + word
    if suffix is not None:
        word = word + f"__{suffix}"
    return word


class Walkforward:
    @staticmethod
    def generate_walk_forward_interval(
            stride: int,
            last_date: Union[str],
            t_end_testing: Union[str],
            t_start_testing: Union[str],
            t_start_validating: Union[str],
            t_start_training: Union[str],
            overlap: bool = False,
            mode: str = 'expanding',
            prefix: Optional[str] = None,
            suffix: Optional[str] = None
    ):
        time = {
            "t_end_testing": t_end_testing,
            "t_start_testing": t_start_testing,
            "t_start_validating": t_start_validating,
            "t_start_training": t_start_training}

        time = time.copy()
        last_date = datetime.strptime(last_date, '%Y-%m-%d')

        for key in time.keys():
            time[key] = datetime.strptime(time[key], '%Y-%m-%d')

        if not overlap:
            time['t_end_testing'] = time['t_start_testing'] + timedelta(days=stride)

        times = OrderedDict()
        Exit = False
        while Exit == False:
            futureTime = time['t_end_testing'] + timedelta(days=stride)
            if futureTime >= last_date:
                Exit = True

            if mode == 'expanding':
                KEYS = ['t_start_validating', 't_start_testing', 't_end_testing']
            else:
                KEYS = ['t_start_training', 't_start_validating', 't_start_testing', 't_end_testing']

            store = {}
            for key in time.keys():
                store[key] = time[key]

            key = _add_affixes(datetime2str(time['t_end_testing']), prefix, suffix)
            times[key] = store.copy()
            for key in KEYS:
                time[key] = time[key] + timedelta(days=stride)

        # change last key with the last date
        last_key = next(reversed(times))
        new_last_key = _add_affixes(datetime2str(last_date), prefix, suffix)
        times[last_key]['t_end_testing'] = last_date
        times[new_last_key] = times.pop(last_key)
        return times


def get_intervals(
        t_start_validating: str = "2021-06-27",
        t_start_training: str = "2020-06-27"
):
    walkforward_intervals = Walkforward().generate_walk_forward_interval(
        stride=60,
        last_date="2022-10-27",
        t_end_testing="2021-10-27",
        t_start_testing="2021-08-27",
        t_start_validating=t_start_validating,
        t_start_training=t_start_training,
        overlap=False,
        mode='following',
        prefix="period"
    )
    return walkforward_intervals


if __name__ == '__main__':
    walkforward_intervals = get_intervals()
    for val in walkforward_intervals.values():
        print('t_end_testing -> t_start_testing: ', (val['t_end_testing'] - val['t_start_testing']).days)
        print('t_start_testing -> t_start_validating: ', (val['t_start_testing'] - val['t_start_validating']).days)
        print('t_start_validating -> t_start_training: ', (val['t_start_validating'] - val['t_start_training']).days)
    for name, time in walkforward_intervals.items():
        print(name, time)
