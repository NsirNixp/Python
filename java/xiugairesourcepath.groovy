import com.eviware.soapui.impl.rest.RestResource

def project = testRunner.testCase.testSuite.getProject()
String restServiceName = "http://bangumi.bilibili.com"
List<RestResource> ops = project.getInterfaces()[restServiceName].getOperationList()


//project.getInterfaces()[restServiceName].setBasePath("http://bangumi.bilibili.com")

for (RestResource res : ops)
{
    res.each{
        op -> toggleDebug(op)
    }
}

public void toggleDebug(RestResource op){
    String path = op.getFullPath();
	if(path.contains("@")){
		def season_id = context.expand( '${testdata#season_id}' )
		path = path.replace("@",season_id)
	}
	op.setPath(path)
	log.info op.getPath()
}
//    if ( path.contains("&debug") || path.contains("?debug") ){
//        if (path.contains("&debug")){
//                path = path.replaceAll("&debug","")
//            }
//        if (path.contains("/?debug")){
//                path = path.replaceAll("\\?debug","")
//            }
//        op.setPath(path)
//        log.info op.getPath()
//        log.info "DEBUG mode DISABLED for operation: '" + op.getName() + "'. New path: "  + path
//    }
//    else{
//        if (path.contains("?")){
//                path += "&debug"
//            }else{
//                path += "?debug"
//            }
//        op.setPath(path)
//        log.info "DEBUG mode ENABLED for operation: '" + op.getName() + "'. New path: "  + path
//    }

log.info ops[13]