$(document).ready(function() {
    $(".grid-view table tbody").find('a[data-method="POST"]').each(function() {
        $(this).click(function() {
            var confirmTxt = $(this).attr('data-confirm');
            if(confirm(confirmTxt)) {
                var url = $(this).attr('data-url');
                var form = document.createElement('form');
                var csrfInput = document.createElement('input');
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = $.cookie('csrftoken');
                form.appendChild(csrfInput);

                form.method = "post";
                form.action = url;
                form.style.display = 'none';
                document.body.append(form);
                form.submit();
                return form;
            }
            return false;
        })
    });

    $(".tree-grid-view .tree-grid li").find('a[data-method="POST"]').each(function() {
        $(this).click(function() {
            var confirmTxt = $(this).attr('data-confirm');
            if(confirm(confirmTxt)) {
                var url = $(this).attr('data-url');
                var form = document.createElement('form');
                var csrfInput = document.createElement('input');
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = $.cookie('csrftoken');
                form.appendChild(csrfInput);

                form.method = "post";
                form.action = url;
                form.style.display = 'none';
                document.body.append(form);
                form.submit();
                return form;
            }
            return false;
        })
    });

    g_object_ids = new Array(); // 多文件上传图片返回的id
    g_object_urls = new Array(); // 多文件上传图片返回的url
    $('.media-picker').each(function() {
        var el = $(this);
        var elbtn = el.find('.media-picker-button');
        var multi_selection = false;
        // 上传目录
        var inputField = el.find('input[type=hidden]');

        var token = $.cookie('csrftoken');
 
        // 是否多文件上传
        if (elbtn.attr('data-multiple') == 'multiple') {
            multi_selection = true;
        }
        var updir = elbtn.attr('data-upload-path');
        var uploader = new plupload.Uploader({
            runtimes : 'html5,flash,silverlight,html4',
            browse_button : elbtn.attr('data-id') + '_uploader', 
            url : '/backend/upload',
            file_data_name: 'image',
            multi_selection: multi_selection,
            multipart_params: { 'updir': updir, 'csrfmiddlewaretoken': token },
            auto_start: true,
            flash_swf_url : '../plugins/plupload/Moxie.swf',
            silverlight_xap_url : '../plugins/plupload/Moxie.xap',
            
            filters : {
                max_file_size : '10mb',
                prevent_duplicates: false,
                mime_types: [
                    {title : "Image files", extensions : "jpg,gif,png"},
                    {title : "Video files", extensions : "mp4"}
                ]
            },
        
            init: {
                FilesAdded: function(up, files) {
                    up.start(); //选择完后直接上传
                },
        
                FileUploaded: function(up, file, info) {
                    if (info.status == 200) {
                        var file_infos = $.parseJSON(info.response);
                        if(file_infos.errno == 200) {
                            var file_url = file_infos.url;
                            var file_id = file_infos.id;
                            console.log(file_id)
                            var imageHtml = '';
                            if (multi_selection) {
                                g_object_urls.push(file_url);
                                g_object_ids.push(file_id)
                                inputField.val(JSON.stringify(g_object_ids));
                                for(var i = 0; i< g_object_ids.length; i++) {
                                    imageHtml += '<li><img src="' + g_object_urls[i] + '"/><div data-url="' + g_object_urls[i] + '" data-id="' + g_object_ids[i] + '" class="delete-image"> X </div></li>';
                                }
                            } else {
                                inputField.val(file_id);
                                var imageHtml = '';
                                imageHtml = '<li><img src="' + file_url + '"/><div data-id="' + file_id + '" class="delete-image"> X </div></li>';
                                
                            }
                            el.find('.media-list ul').html(imageHtml);
                        } else {
                            alert(file_infos.data)
                        }
                       
                        
                    } else {
                        alert(info.response);
                    }
                },
        
                Error: function(up, err) {
                    console.log(err.code)
                    console.log(err.message)
                }
            }
        });
        
        uploader.init();
    })

    $('.media-picker').each(function() {
        var el = $(this)
        var inputField = el.find('input[type=hidden]');
        var elbtn = el.find('.media-picker-button');
        var multi_selection = false;
        // 是否多文件上传
        if (elbtn.attr('data-multiple') == 'multiple') {
            multi_selection = true;
        }
        if(multi_selection) {
            el.on('click', '.delete-image', function() {
                // 后台不做删除，可在后台禁用
                var currentId = $(this).attr('data-id');
                var currentUrl = $(this).attr('data-url');
                // 删除当前的父级li
                $(this).parent().remove();
                // 重新赋值数组
                // 去掉url数组中的当前url
                for(var i in g_object_urls) {
                    if(g_object_urls[i] == currentUrl) {
                        g_object_urls.splice(i, 1);
                        break;
                    }
                }
                // 去掉id数组中的当前id
                for(var i in g_object_ids) {
                    if(g_object_ids[i] == currentId) {
                        g_object_ids.splice(i, 1);
                        break;
                    }
                }
                inputField.val(JSON.stringify(g_object_ids));
            })
        } else {
            el.on('click', '.delete-image', function() {
                // 显示值为空, 后台不做删除，可在后台禁用
                el.find('.media-list ul').html('');
                inputField.val('');
            })
        }

    })
    
})