from setuptools import setup, find_packages

setup(
    name='qa_server',  # 你的包名
    version='0.1.0',  # 版本号
    description='quantaxis support for ctpbee',  # 包的简短描述
    long_description=open('README.md').read(),  # 长描述，通常从 README.md 读取
    long_description_content_type='text/markdown',  # 长描述的内容类型
    author='somewheve',  # 作者名
    author_email='somewheve@gmail.com',  # 作者邮箱
    url='https://github.com/ctpbee/qa_server',  # 项目主页，通常是 GitHub 仓库链接
    packages=find_packages(where='qa_server'),  # 自动发现包，指定源码目录
    package_dir={'': 'qa_server'},  # 指定包的根目录
    install_requires=[  # 依赖项列表
        'ctpbee',
    ],
    classifiers=[  # 分类器，用于 PyPI 上的分类
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',  # Python 版本要求
    include_package_data=True,  # 包含包数据文件
    license='MIT',  # 许可证类型
    keywords='对接quantaxis下单接口',  # 关键词
)
