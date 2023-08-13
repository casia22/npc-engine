# 这部分代码保证项目能被python解释器搜索到
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from npc_engine import NPCEngine

if __name__ == '__main__':
    engine = NPCEngine()