from CurveManager import CurveManager
from CurveManager1 import CurveManager1
from BarManager import BarManager
from BarManager1 import BarManager1

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # pressureCurves = CurveManager()
    # pressureCurves.process_all_csv_files()
    # pressureCurves.draw_main_figure()

    # pressureCurves = CurveManager1()
    # pressureCurves.process_all_csv_files()

    # barManager = BarManager()
    # barManager.run()

    barManager = BarManager1()
    barManager.run()