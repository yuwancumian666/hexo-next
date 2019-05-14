{%
  set js_commons = [
    'utils.js',
    'motion.js'
  ]
%}

<!-- 一言
<script type="text/javascript">
	$.get('https://v1.hitokoto.cn/?c=c', function (data) {
		$('#hitokoto-content').css('display', '').text(data.hitokoto);
		$('#hitokoto-from').css('display', '').text('——' + data.from);
	});
</script>-->

<!-- Loline 服务器请求方式
<script type="text/javascript">
	$.get('https://149.129.113.178:5000/', function (data) {
    console.log('----------------------------------------')
    console.log(data)
		$('#loline-content').css('display', '').text(data.words);
		$('#loline-from').css('display', '').text('——' + data.title_zh+' '+data.name_zh);
	});
</script>
-->
<!-- Loline 加载本地json文件方式 -->
<script type="text/javascript">
	$.get("/json/champions.json", function (data) {
    console.log('url: '+'{{ url }}');
		// champions = JSON.parse(data);
		var ranint = function(min, max) {
    	return Math.round(Math.random() * (max - min)) + min;
		}(1, data.length);
		champion = data[ranint-1];
		console.log(ranint);
		console.log(champion);
		$('#loline-content').css('display', '').text(champion.words);
		$('#loline-from').css('display', '').text('——' + champion.title_zh+' '+champion.name_zh);
	});
</script>


{% for common in js_commons %}
  <script src="{{ url_for(theme.js) }}/{{ common }}?v={{ version }}"></script>
{% endfor %}
