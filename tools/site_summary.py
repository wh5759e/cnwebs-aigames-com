import json
from datetime import datetime


SITE_DATA = [
    {
        "name": "爱游戏体育",
        "url": "https://cnwebs-aigames.com",
        "tags": ["体育", "电竞", "赛事"],
        "description": "综合体育与电子竞技资讯平台，提供实时比分、赛事分析和最新动态。",
        "keywords": ["爱游戏体育", "体育资讯", "电竞比分", "赛事预测"],
    },
    {
        "name": "极速体育",
        "url": "https://www.fast-sports.cn",
        "tags": ["体育", "快讯", "数据"],
        "description": "专注于体育快讯与数据统计，覆盖足球、篮球等主流项目。",
        "keywords": ["极速体育", "体育快讯", "足球数据", "篮球统计"],
    },
    {
        "name": "电竞观察",
        "url": "https://www.esports-insight.net",
        "tags": ["电竞", "深度", "分析"],
        "description": "深度报道电竞赛事、战队动态及行业趋势，为玩家提供专业视角。",
        "keywords": ["电竞观察", "电竞赛事", "战队动态", "行业分析"],
    },
]


def create_summary(entry):
    """生成单条站点摘要字典"""
    return {
        "site_name": entry["name"],
        "site_url": entry["url"],
        "tags": entry["tags"],
        "description": entry["description"],
        "keywords": entry["keywords"],
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def format_summary_text(summary):
    """将摘要字典格式化为可读文本"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"站点名称：{summary['site_name']}")
    lines.append(f"站点URL：{summary['site_url']}")
    lines.append(f"标签：{', '.join(summary['tags'])}")
    lines.append(f"关键词：{', '.join(summary['keywords'])}")
    lines.append(f"简短说明：{summary['description']}")
    lines.append(f"摘要生成时间：{summary['generated_at']}")
    lines.append("=" * 60)
    return "\n".join(lines)


def generate_all_summaries(data):
    """为所有站点生成摘要列表"""
    summaries = []
    for item in data:
        summary = create_summary(item)
        summaries.append(summary)
    return summaries


def export_summaries_as_json(summaries, filepath="site_summaries.json"):
    """将摘要列表导出为 JSON 文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summaries, f, ensure_ascii=False, indent=2)
    print(f"摘要已导出至 {filepath}")


def display_summaries_verbose(summaries):
    """在控制台打印所有摘要文本"""
    for idx, summ in enumerate(summaries, start=1):
        print(f"\n--- 站点摘要 #{idx} ---")
        print(format_summary_text(summ))


def main():
    print("站点资料结构化摘要生成器")
    print("处理站点数量：", len(SITE_DATA))
    summaries = generate_all_summaries(SITE_DATA)
    display_summaries_verbose(summaries)
    export_summaries_as_json(summaries)
    print("\n所有站点摘要处理完成。")


if __name__ == "__main__":
    main()